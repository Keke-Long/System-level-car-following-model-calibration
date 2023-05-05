# -*- coding: utf-8 -*-
"""
@author: Keke
"""
import pandas as pd

df = pd.read_csv("../Data/Veh_info3.csv")
import numpy as np
import sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# 车辆长度列表
vehicle_lengths = df['length']
# 将列表转换为 NumPy 数组
X = np.array(vehicle_lengths).reshape(-1, 1)
# 使用 K-Means 算法进行聚类，分为 3 类
n=2
kmeans = KMeans(n_clusters=n, random_state=0).fit(X)
# 打印每个聚类的质心和聚类结果
plt.scatter(X, np.zeros(len(X)), c=kmeans.labels_, cmap='viridis')
# 绘制聚类中心
plt.scatter(kmeans.cluster_centers_,[0]*n, s=200, alpha=0.5, c=range(n), cmap='viridis')
plt.show()
# 打印聚类中心
print("Cluster 1 centroid:", kmeans.cluster_centers_[0][0])
print("Cluster 2 centroid:", kmeans.cluster_centers_[1][0])
# 第一类的最大值
cluster_1 = X[kmeans.labels_ == 0]
max_value = np.max(cluster_1)
print("The maximum value of cluster 1:", max_value)

