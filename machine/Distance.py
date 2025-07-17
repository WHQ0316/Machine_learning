"""
    计算两个向量的距离：
        1、欧几里得距离 (L2距离)
        2、曼哈顿距离 (L1距离)
        3、闵可夫斯基距离：欧几里得距离和曼哈顿距离的泛化形式
        4、马哈拉诺比斯距离：考虑特征间相关性的距离度量
"""
# %% 导入相关文件
import numpy as np

# %% 距离函数

# 欧几里得距离
def euclidean_distance(data_x, data_y):
    return np.sqrt(np.sum((data_x - data_y) ** 2))
# 曼哈顿距离
def manhattan_distance(data_x, data_y):
    return np.sum(np.abs(data_x - data_y))
# 闵可夫斯基距离
def minkowski_distance(data_x, data_y, p):
    # (p=1是曼哈顿距离，p=2是欧几里得距离)
    return np.sum(np.abs(data_x - data_y) ** p) ** (1 / p)
# 马哈拉诺比斯距离(目前没有用到)
def mahalanobis_distance(data_x, data_y, cov_matrix):
    diff = data_x - data_y
    inv_cov = np.linalg.inv(cov_matrix)
    return np.sqrt(diff.T @ inv_cov @ diff)

# %% 测试
# X = np.array([1, 0, 1, 1, 0])
# Y = np.array([1, 1, 0, 1, 1])
# X_Y_1 = euclidean_distance(X, Y)  # p=2  欧几里得距离
# X_Y_2 = manhattan_distance(X, Y)  # p=1  曼哈顿距离
# X_Y_3 = minkowski_distance(X, Y, p=1)
# print("euclidean_distance:", X_Y_1, '\n', "manhattan_distance:", X_Y_2, '\n', "minkowski_distance:", X_Y_3, '\n')

