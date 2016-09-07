import numpy as np

digit_mat_sz = np.array([31, 11]) 
dim_x = digit_mat_sz[0]*digit_mat_sz[1]
dim_y = 1
dim_y_normed = 10

def norm_y(y):
    n = y.shape[0]
    one_hot = np.zeros((n, dim_y_normed))
    one_hot[range(n), y] = 1
    return one_hot.reshape((n, -1))
