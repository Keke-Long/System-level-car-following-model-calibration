# -*- coding: utf-8 -*-
"""
Apply eco-driving at corridor
@author: Keke Long
"""

from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import optparse
import pandas as pd
import numpy as np
import math

from SUMO.traci_route_add import traci_route_add
from SUMO.traci_vehicle_add import traci_vehicle_add
from SUMO.traci_vtype_add import traci_vtype_add

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

def get_options():
    optParser = optparse.OptionParser() 
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options
def simulate_traffic(veh_info, time_simulation=5000):

    options = get_options()
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')
    traci.start([sumoBinary, "-c", "../SUMO/ParkSt.sumocfg"])

    traci_route_add()
    traci_vtype_add() # set CF models
    route_list = traci.route.getIDList()
    traci_vehicle_add(veh_info, route_list)

    # Simulation
    df = pd.DataFrame(columns=['time', 'vehicle', 'x', 'y', 'speed', 'acceleration']) # save trj
    for step in range(0, time_simulation):
        t = step/10
        print("\rt = %.1f" % t)#, end='')


        # CAV control
        # 针对交叉口1得到进口道所有车的：位置速度转向
        node1_entrance_edge = ['I0I1','I2I1','I5I1']
        node1_veh_list = []
        for edge in node1_entrance_edge:
            veh_on_edge = traci.edge.getLastStepVehicleIDs(edge)
            node1_veh_list += veh_on_edge
        node1_veh = pd.DataFrame(columns=['x', 'v', 'a', 'edge'])
        for id in node1_veh_list:
            x = traci.vehicle.getLanePosition(id)
            v = traci.vehicle.getSpeed(id)
            a = traci.vehicle.getAcceleration(id)
            edge = traci.vehicle.getRoadID(id)
            node1_veh.loc[id] = [x, v, a, edge]
        # 然后计算每一辆车的最早到达时间

        # 计算所有车的实际到达时间，可以FCFS也可以优化一下，烦这个解决一下左转和直行冲突的问题就可以了，

        # 根据实际到达时间确定车辆轨迹

        # 得到当前信号灯状态
        I1_plan = [45,3,36,3] # I1的四个相位：0东西，1黄灯，2北，3黄灯
        light = traci.trafficlight.getPhase('I1')
        print(t, 'light', light)
        # 确定所有车的到达时间,东西相位的左转要担心冲突，
        # 针对每一个相位，看哪些车能到，能到的就分配位置，然后下一个相位，直到所有车都确定到达时间，




        # Save simulated_trj
        vehicle_list = traci.vehicle.getIDList()
        for vehicle_id in vehicle_list:
            x, y = traci.vehicle.getPosition(vehicle_id)
            v = traci.vehicle.getSpeed(vehicle_id)
            a = traci.vehicle.getAcceleration(vehicle_id)
            df = df.append({'t': t, 'id': vehicle_id, 'x': x, 'y': y, 'v': v, 'a': a}, ignore_index=True)

        traci.simulationStep()
    traci.close()
    #df.to_csv('../Data/Simulated_trj_data.csv', index=False)
    return df

'''
After Simulation: Analysis Part
'''
def VT_Micro(v,a):
    PE = np.matrix([[-8.27978, 0.36696, -0.04112, 0.00139],
                    [0.06229, -0.02143, 0.00245, 3.71 * 10 ** (-6)],
                    [-0.00124, 0.000518, 6.77 * 10 ** (-6), -7.4 * 10 ** (-6)],
                    [7.72 * 10 ** (-6), -2.3 * 10 ** (-6), -5 * 10 ** (-7), 1.05 * 10 ** (-7)]])

    NE = np.matrix([[-8.27978, -0.27907, -0.05888, -0.00477],
                    [0.06496, 0.03282, 0.00705, 0.000434],
                    [-0.00131, -0.00066, -0.00013, -7.6 * 10 ** (-6)],
                    [8.23 * 10 ** (-6), 3.54 * 10 ** (-6), 6.48 * 10 ** (-7), 3.98 * 10 ** (-8)]])

    PE2 = np.matrix([[-0.679439, 0.135273, 0.015946, -0.001189],
                     [0.029665, 0.004808, -0.000020635, 5.5409285 * 10 ** (-8)],
                     [-0.000276, 0.000083329, 0.000000937, -2.479644 * 10 ** (-8)],
                     [0.000001487, -0.000061321, 0.000000304, -4.467234 * 10 ** (-9)]])
    a = a * 3.6 # m/s to km/h
    v = v * 3.6
    if a >= 0:
        fuel = np.power(math.e, np.matrix([1, v, np.power(v,2), np.power(v,3)]) * PE * np.transpose(np.matrix([1, a, np.power(a,2), np.power(a,3)])) )
    else:
        fuel = np.power(math.e, np.matrix([1, v, np.power(v,2), np.power(v,3)]) * NE * np.transpose(np.matrix([1, a, np.power(a,2), np.power(a,3)])) )
    return fuel[0,0]
def Cal_travel_fuel(group, utm_pts, distance_threshold):
    distances = np.sqrt((group['x'] - utm_pts[:, 0])**2 + (group['y'] - utm_pts[:, 1])**2)
    is_within_range = distances < distance_threshold

    # 如果没有进入指定范围内，则返回空的 Series
    if not is_within_range.any():
        return pd.Series({'entry_time': np.nan, 'exit_time': np.nan, 'travel_time': np.nan, 'fuel': np.nan})

    # 找到第一个进入指定范围内的行,最后一个离开指定范围内的行
    entry_row = group[is_within_range].iloc[0]
    entry_time = entry_row['t']

    exit_row = group[is_within_range].iloc[-1]
    exit_time = exit_row['t']

    # 如果该车有位置记录在进入区域前，且有离开区间后的记录，则计算它的行驶时间
    if is_within_range.iloc[0] == False and is_within_range.iloc[-1] == False:
        first_row = group.iloc[0]
        last_row = group.iloc[-1]
        travel_time = exit_time - entry_time
        v = group.loc[entry_row.name:last_row.name, 'v'].values
        a = group.loc[entry_row.name:last_row.name, 'a'].values
        fuel = sum([VT_Micro(v[i], a[i]) for i in range(len(v))])
    else:
        travel_time = 0
        fuel = 0

    # 返回进入和离开时间以及行驶时间
    return pd.Series({'entry_time': entry_time, 'exit_time': exit_time, 'travel_time': travel_time, 'fuel': fuel/len(group['id'].unique())})
def analysis_simulated_trj(df):
    # 定义交叉口中心
    Intersection_utm = [[0, 0],
                        [130, -7],
                        [258, -14]]

    df['distance_to_I1'] = np.sqrt((df['x'] - Intersection_utm[0][0])**2 + (df['y'] - Intersection_utm[0][1])**2)
    df['distance_to_I2'] = np.sqrt((df['x'] - Intersection_utm[1][0])**2 + (df['y'] - Intersection_utm[1][1])**2)
    df['distance_to_I3'] = np.sqrt((df['x'] - Intersection_utm[2][0])**2 + (df['y'] - Intersection_utm[2][1])**2)

    df['time_period'] = (df['t']-600) // (60*15) #15分钟一个时段
    distance_threshold = 70

    # 计算第一个指定范围内的结果
    entry_exit_times_I1 = df.groupby(['id', 'time_period']).apply(Cal_travel_fuel, np.array([Intersection_utm[0]]), distance_threshold)
    avg_travel_time_I1 = entry_exit_times_I1.groupby('time_period')['travel_time'].mean()
    avg_fuel_I1 = entry_exit_times_I1.groupby('time_period')['fuel'].mean()

    # 计算第二个指定范围内的结果
    entry_exit_times_I2 = df.groupby(['id', 'time_period']).apply(Cal_travel_fuel, np.array([Intersection_utm[1]]), distance_threshold)
    avg_travel_time_I2 = entry_exit_times_I2.groupby('time_period')['travel_time'].mean()
    avg_fuel_I2 = entry_exit_times_I2.groupby('time_period')['fuel'].mean()

    # 计算第三个指定范围内的结果
    entry_exit_times_I3 = df.groupby(['id', 'time_period']).apply(Cal_travel_fuel, np.array([Intersection_utm[2]]), distance_threshold)
    avg_travel_time_I3 = entry_exit_times_I3.groupby('time_period')['travel_time'].mean()
    avg_fuel_I3 = entry_exit_times_I3.groupby('time_period')['fuel'].mean()

    # 将结果保存到 CSV 文件
    result_df = pd.DataFrame({
        # result['start_time'] = result.index * (60 * 10)
        # result['end_time'] = (result.index + 1) * (60 * 10) - 1
        'avg_travel_time_I1': round(avg_travel_time_I1, 3),
        'avg_travel_time_I2': round(avg_travel_time_I2, 3),
        'avg_travel_time_I3': round(avg_travel_time_I3, 3),
        'avg_fuel_I1': round(avg_fuel_I1, 3),
        'avg_fuel_I2': round(avg_fuel_I2, 3),
        'avg_fuel_I3': round(avg_fuel_I3, 3)
    })
    result_df.to_csv('../Data/Simulated_result.csv', index_label='time_period')
def sim_corridor(veh_info):
    df = simulate_traffic(veh_info, time_simulation=5000)
    result = analysis_simulated_trj(df)
    return result


veh_info = pd.read_csv("../Data/Veh_info3.csv")
sim_corridor(veh_info)