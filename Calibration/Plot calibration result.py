# 给定车辆id， 画图，预测加速度和实际加速度，用
import matplotlib.pyplot as plt
import pandas as pd
from IDM import IDM

def plot_comparison(df, car_id, save_file=None):
    d = df[(df['id'] == car_id)]
    # vf, A, b, s0, T
    arg = (17.01441366, 2.11620502, 1.69595889, 1.77614233, 1.46909532)
    d['ahat'] = d.apply(lambda row: IDM(arg, row['v'], row['v'] - row['pre_v'], row['delta_d']), axis=1)
    d['vhat'] = d['v'] + d['ahat']

    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    # 绘制速度对比图
    axs[0].plot(d['t_sec'], d['v'], label='Real v')
    axs[0].plot(d['t_sec'], d['vhat'], label='Predicted v')
    axs[0].set_xlabel('Time (seconds)')
    axs[0].set_ylabel('Speed (m/s)')
    axs[0].legend()
    axs[0].set_title('Vehicle %d Speed Comparison' % car_id)

    # 绘制加速度对比图
    axs[1].plot(d['t_sec'], d['a'], label='Real a')
    axs[1].plot(d['t_sec'], d['ahat'], label='Predicted a')
    axs[1].set_xlabel('Time (seconds)')
    axs[1].set_ylabel('Acceleration (m/s^2)')
    axs[1].legend()
    axs[1].set_title('Vehicle %d Acceleration Comparison' % car_id)

    plt.subplots_adjust(hspace=0.4)

    if save_file:
        plt.savefig('%d_comparison.jpg' % car_id)
    plt.show()


df = pd.read_csv("../Data/Data3_lane_xy_va_pre_clean.csv")
id = 150
d = df[(df['id'] == id)]
plot_comparison(d, id, save_file=True)
