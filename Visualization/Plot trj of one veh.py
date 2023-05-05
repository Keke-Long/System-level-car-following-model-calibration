import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Data/Data3_lane_xy_va_pre.csv")
id = 3094
d = df[df['id'] == id]

fig, ax = plt.subplots(figsize=(10, 8))
# 绘制散点图，并设置颜色和颜色映射
sc = ax.scatter(d['x_utm'], d['y_utm'], c=d['t_sec'], cmap='viridis')
ax.set_title(r"%s辆车" % id)
ax.set_xlabel('X_UTM (m)')
ax.set_ylabel('y_UTM (m)')
ax.invert_yaxis()
ax.axis('equal')

# 添加颜色条
cbar = fig.colorbar(sc)
cbar.ax.set_ylabel('Time (s)')

# 显示图形
plt.show()


