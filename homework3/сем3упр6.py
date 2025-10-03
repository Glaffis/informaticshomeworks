import numpy as np
def mnk_cf(N, sigma, k, b):
    x = np.array(range(N))
    f = np.array([k*i+b for i in range(N)])
    y = f + np.random.normal(0, sigma, N)
    x_sum = x.sum()/N
    y_sum = y.sum()/N
    a2 = np.dot(x.T, x)/N
    a11 = np.dot(x.T, y)/N 
    kk = (a11 - x_sum*y_sum)/(a2 - x_sum**2)
    bb = y_sum - kk*x_sum
    print(kk, bb)

mnk_cf(10, 2, 5, 4) #пример