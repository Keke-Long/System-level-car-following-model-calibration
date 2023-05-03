import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IDM import IDM


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


class PSO:
    def __init__(self, parameters):
        """
        particle swarm optimization
        parameter: a list type, like [NGEN, pop_size, var_num_min, var_num_max]
        """
        self.NGEN = parameters[0]  # 迭代的代数
        self.pop_size = parameters[1]  # 种群大小
        self.var_num = len(parameters[2])  # 变量个数
        self.bound = []  # 变量的约束范围
        self.bound.append(parameters[2])
        self.bound.append(parameters[3])

        self.pop_x = np.zeros((self.pop_size, self.var_num))  # 所有粒子的位置
        self.pop_v = np.zeros((self.pop_size, self.var_num))  # 所有粒子的速度
        self.p_best = np.zeros((self.pop_size, self.var_num))  # 每个粒子最优的位置
        self.g_best = np.zeros((1, self.var_num))[0]  # 全局最优的位置

        # 初始化第0代初始全局最优解
        temp = 1000000000000000000
        for i in range(self.pop_size):
            for j in range(self.var_num):
                self.pop_x[i][j] = random.uniform(self.bound[0][j], self.bound[1][j])
                self.pop_v[i][j] = random.uniform(0, 1)
            self.p_best[i] = self.pop_x[i]  # 储存最优的个体
            fit = self.fitness(self.p_best[i])
            if fit < temp:
                self.g_best = self.p_best[i]
                temp = fit

    def fitness(self, ind_var):
        """
        个体适应值计算 IDM模型
        """
        vf = ind_var[0] # free flow speed
        A  = ind_var[1]
        b  = ind_var[2]
        s0 = ind_var[3]
        T  = ind_var[4]
        arg = (vf, A, b, s0, T)
        error=[]
        for i in range(self.pop_size):
            ai = df.iloc[i]['a'] # 本车a
            vi = df.iloc[i]['v'] # 本车v
            delta_v = df.iloc[i]['v'] - df.iloc[i]['pre_v'] # velocity difference, subject vehicle - pre vehicle
            delta_d = df.iloc[i]['delta_d'] # distance (without length of vehicles)
            ahat = IDM(arg, vi, delta_v, delta_d)
            error.append((ai-ahat)**2)
        y = np.mean(error)
        return y

    def update_operator(self, pop_size):
        """
        更新算子：更新下一时刻的位置和速度
        """
        c1 = 2  # 学习因子，一般为2
        c2 = 2
        w = 0.4  # 自身权重因子
        for i in range(pop_size):
            # 更新速度
            self.pop_v[i] = w * self.pop_v[i] + c1 * random.random() * (self.p_best[i] - self.pop_x[i]) + c2 * random.random()*(self.g_best - self.pop_x[i])
            # 更新位置
            self.pop_x[i] = self.pop_x[i] + self.pop_v[i]
            # 越界保护
            for j in range(self.var_num):
                if  self.pop_x[i][j] < self.bound[0][j]:
                    self.pop_x[i][j] = self.bound[0][j]
                if  self.pop_x[i][j] > self.bound[1][j]:
                    self.pop_x[i][j] = self.bound[1][j]
            # 更新p_best和g_best
            if self.fitness(self.pop_x[i]) < self.fitness(self.p_best[i]):
                self.p_best[i] = self.pop_x[i]
            if self.fitness(self.pop_x[i]) < self.fitness(self.g_best):
                self.g_best = self.pop_x[i]

    def main(self):
        popobj = []
        self.ng_best = np.ones((1, self.var_num))[0]
        prev_fitness = 0
        for gen in range(self.NGEN):
            self.update_operator(self.pop_size)
            popobj.append(self.fitness(self.g_best))
            print('### Generation {} ###'.format(str(gen + 1)))
            if self.fitness(self.g_best) < self.fitness(self.ng_best):
                self.ng_best = self.g_best.copy()
            print('Best parameters: {}'.format(self.ng_best))
            print('Best result: {}'.format(self.fitness(self.ng_best)))
            if abs(self.fitness(self.g_best) - prev_fitness) < 0.00001:
                print("Stopping loop: fitness difference is less than 0.00001")
                break
            prev_fitness = self.fitness(self.g_best)
        print("Final result", self.ng_best)
        print("--- End of (successful) Searching ---")

        plt.figure()
        plt.title("Figure1")
        plt.xlabel("iterators", size=14)
        plt.ylabel("fitness", size=14)
        t = [t for t in range(len(popobj))]
        plt.plot(t, popobj, color='b', linewidth=2)
        plt.show()


if __name__ == '__main__':

    # Data clean
    df = pd.read_csv("../Data/Data3_lane_xy_va_pre.csv")
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

    # Calibration
    NGEN = 100
    popsize = 20
    CF_model = 'IDM'
    low = [10,2,1,0.1,0.1] # vf, a, b, s0, T
    up =  [40,6,3, 3,  5]
    parameters = [NGEN, popsize, low, up]
    pso = PSO(parameters)
    pso.main()
