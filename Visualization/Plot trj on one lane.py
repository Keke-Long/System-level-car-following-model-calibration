import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Data/Data3_lane_xy_va_pre.csv")

d = df[(df['edge'] == '3_2') & (df['lane'] == 0)]
# 按照车辆id将数据分组
groups = d.groupby('id')

# 为每一辆车创建一个子图
fig, ax = plt.subplots(figsize=(20, 8))

# 遍历每一辆车，使用plot()函数将其x_utm值随时间的变化结果用折线连接
for car_id, group in groups:
    ax.plot(group['t_sec'], group['x_utm'], label=f"Car {car_id}")

# 添加图形标题、x轴标签和y轴标签
ax.set_title('X_UTM over Time for Car {car_id}')
ax.set_xlabel('Time')
ax.set_ylabel('X_UTM')
ax.set_xlim([600, 600+15*60])

# 显示图形
plt.legend()
plt.show()






