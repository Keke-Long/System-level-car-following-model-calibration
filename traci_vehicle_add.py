# -*- coding: utf-8 -*-
"""
@author: Keke
"""

import traci
import pandas as pd


# 车辆长度判断阈值 7.9
def traci_vehicle_add(df, route_list):
    for index, row in df.iterrows():
        id = str(row['id'])
        depart_time = row['start_time']

        if row['length'] < 7.9:
            veh_type = "HV_IDM_s"
            depart_Lane = 1
        else:
            veh_type = "HV_IDM_l"
            depart_Lane = 0

        if row['edge_start'][0] != 'n' and row['edge_end'][0] != 'n':
            start_edge = row['edge_start'].split('_')[0]
            end_edge = row['edge_end'].split('_')[1]
            route = 'S'+start_edge+'E'+end_edge
            if route in route_list:
                print('id',id, 'route', route, "depart_time", depart_time, 'veh_type', veh_type, "depart_Lane", depart_Lane)
                traci.vehicle.add(id, route, typeID=veh_type, depart=depart_time, departSpeed=12, departLane=depart_Lane)

