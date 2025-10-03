import numpy as np
import random
def data_random(N, a, b, sigma):
    x = np.arange(N)
    y = np.array([a * xi + b + random.gauss(0, sigma) for xi in x])
    return x, y
data_random (30, 2, 4, 1) #пример