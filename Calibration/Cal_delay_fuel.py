"""
用实际轨迹计算10分钟的中观油耗和travel time
"""
import pandas as pd
import numpy as np
import math
import utm

df = pd.read_csv('Data1_lane_xy_va_pre.csv')

# 定义指定范围
Intersection_GPS = [[43.0733, -89.4006],
                    [43.0721, -89.4008],
                    [43.0710, -89.4008]]

# 经纬度转UTM
def GPS2UTM(GPS_info):
    utmPts = []
    for i in range(len(GPS_info)):
        lat, lon = GPS_info[i][0], GPS_info[i][1]
        utm_ = utm.from_latlon(lat, lon)
        utm_x = utm_[0]
        utm_y = utm_[1]
        utmPts.append([round(utm_x,2) - 300000, round(utm_y,2) - 4770000])
    return utmPts
Intersection_utm = GPS2UTM(Intersection_GPS)
# print('Intersection_utm', Intersection_utm)


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


# 定义计算车辆进入和离开指定范围内的时间的函数
def Cal_travel_fuel(group, utm_pts, distance_threshold):
    distances = np.sqrt((group['x_utm'] - utm_pts[:, 0])**2 + (group['y_utm'] - utm_pts[:, 1])**2)
    is_within_range = distances < distance_threshold

    # 如果没有进入指定范围内，则返回空的 Series
    if not is_within_range.any():
        return pd.Series({'entry_time': np.nan, 'exit_time': np.nan, 'travel_time': np.nan, 'fuel': np.nan})

    # 找到第一个进入指定范围内的行,最后一个离开指定范围内的行
    entry_row = group[is_within_range].iloc[0]
    entry_time = entry_row['t_sec']

    exit_row = group[is_within_range].iloc[-1]
    exit_time = exit_row['t_sec']

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
    return pd.Series({'entry_time': entry_time, 'exit_time': exit_time, 'travel_time': travel_time, 'fuel': fuel})


df['distance_to_I1'] = np.sqrt((df['x_utm'] - Intersection_utm[0][0])**2 + (df['y_utm'] - Intersection_utm[0][1])**2)
df['distance_to_I2'] = np.sqrt((df['x_utm'] - Intersection_utm[1][0])**2 + (df['y_utm'] - Intersection_utm[1][1])**2)
df['distance_to_I3'] = np.sqrt((df['x_utm'] - Intersection_utm[2][0])**2 + (df['y_utm'] - Intersection_utm[2][1])**2)

df['time_period'] = df['t_sec'] // (60*10) #10分钟一个时段
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
    'avg_travel_time_I1': avg_travel_time_I1,
    'avg_travel_time_I2': avg_travel_time_I2,
    'avg_travel_time_I3': avg_travel_time_I3,
    'avg_fuel_I1': avg_fuel_I1,
    'avg_fuel_I2': avg_fuel_I2,
    'avg_fuel_I3': avg_fuel_I3
})
result_df.to_csv('result.csv', index_label='time_period')
