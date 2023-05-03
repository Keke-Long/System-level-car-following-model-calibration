import matplotlib.pyplot as plt
import pandas as pd


def plot_histograms(df, save_file=None):
    fig, axs = plt.subplots(3, 2, figsize=(16, 12))

    # 绘制v的直方图
    axs[0, 0].hist(df['v'], bins=50, color='red', alpha=0.5)
    axs[0, 0].set_title('Distribution of v')
    axs[0, 0].set_xlabel('v (m/s)')
    axs[0, 0].set_ylabel('Counts')

    # 绘制v的直方图_细节
    axs[1, 0].hist(df['v'], bins=50, color='red', alpha=0.5)
    axs[1, 0].set_title('Distribution of v (Part)')
    axs[1, 0].set_xlabel('v (m/s)')
    axs[1, 0].set_ylabel('Counts')
    axs[1, 0].set_ylim([0, 15000])

    # 绘制a的指数直方图
    axs[0, 1].hist(df['a'], bins=100, color='blue', alpha=0.5)
    axs[0, 1].set_title('Distribution of a')
    axs[0, 1].set_xlabel('a (m/s^2)')
    axs[0, 1].set_ylabel('Counts')

    # 绘制a的指数直方图——细节
    axs[1, 1].hist(df['a'], bins=100, color='blue', alpha=0.5)
    axs[1, 1].set_title('Distribution of a (Part)')
    axs[1, 1].set_xlabel('a (m/s^2)')
    axs[1, 1].set_xlim([-20, 20])
    axs[1, 1].set_ylabel('Counts')
    axs[1, 1].set_ylim([0, 20000])

    # 绘制delta_d的直方图
    axs[2, 0].hist(df['delta_d'], bins=50, color='orange', alpha=0.5)
    axs[2, 0].set_xlabel('delta_d (m)')
    axs[2, 0].set_ylabel('Frequency')
    axs[2, 0].set_title('Distribution of delta_d')

    # 绘制t_sec的直方图
    axs[2, 1].hist(df['t_sec'], bins=50, color='green', alpha=0.5)
    axs[2, 1].set_xlabel('travel time (s)')
    axs[2, 1].set_ylabel('Frequency')
    axs[2, 1].set_title('Distribution of travel time')

    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    fig.suptitle(save_file, fontsize=16)

    if save_file:
        plt.savefig(save_file)


def trj_clean(df):
    print("Clean前数据量：", len(df))
    df = df[df['v'].notna()]
    df = df[df['a'].notna()]
    df = df[df['pre_v'].notna()]
    plot_histograms(df, save_file='../Data/histograms_before_clean.png')

    # data cleaning
    df = df[(df['v'] >= 0) & (df['v'] < 16) &
            (df['a'] > -3) & (df['a'] < 3.1) &
            (df['pre_v'] >= 0) & (df['pre_v'] < 16) & (df['delta_d'] > 0)]
    print("Clean后数据量：", len(df))
    plot_histograms(df, save_file='../Data/histograms_after_clean.png')

    print("删除了 %.2f%% 的数据" % ((1 - len(df) / len(pd.read_csv("../Data/Data3_lane_xy_va_pre.csv"))) * 100))
    df.to_csv(path_or_buf="../Data/Data3_lane_xy_va_pre_clean.csv", index=False)
    print('data cleaned')

    return df