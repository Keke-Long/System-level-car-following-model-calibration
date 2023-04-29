"""
显示距离交叉口70的范围是个啥样的范围
"""
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# 读取车辆轨迹数据
df = pd.read_csv('Data1_lane_xy_va_pre.csv')

# 定义指定范围
I1_GPS = [43.0733, -89.4006]
I2_GPS = [43.0721, -89.4008]
I3_GPS = [43.0710, -89.4008]

# 将GPS坐标转换为UTM坐标
import utm
def GPS2UTM(GPS_info):
    lat, lon = GPS_info[0], GPS_info[1]
    utm_ = utm.from_latlon(lat, lon)
    utm_x = utm_[0]
    utm_y = utm_[1]
    return [round(utm_x,2) - 300000, round(utm_y,2) - 4770000]
I1_utm = GPS2UTM(I1_GPS)

# 创建子图
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('equal')

# 将车辆按照id分组
groups = df.groupby('id')

# 遍历所有车辆，绘制车辆轨迹
for name, group in groups:
    # 计算车辆到指定范围的距离
    group['distance_to_I1'] = np.sqrt((group['x_utm'] - I1_utm[0])**2 + (group['y_utm'] - I1_utm[1])**2)

    # 绘制车辆轨迹
    within_range = group['distance_to_I1'] < 50
    within_range_points = group[within_range][['x_utm', 'y_utm']].values
    ax.plot(group['x_utm'], group['y_utm'], 'r-')
    ax.plot(within_range_points[:, 0], within_range_points[:, 1], 'b-')

# 添加标题、坐标轴标签和图例
ax.set_title('Vehicle Trajectories')
ax.set_xlabel('UTM X (m)')
ax.set_ylabel('UTM Y (m)')
ax.legend(loc='best')

# 保存轨迹图像
plt.savefig('vehicle_trajectories.png')

# 关闭图像
plt.close()
