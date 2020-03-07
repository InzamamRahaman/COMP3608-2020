import numpy as np 


num_points = 1000
lambda_p = 1.2 
k = 0.95

data = lambda_p * np.random.weibull(k, size=num_points)

with open('data.npy', 'wb') as fp:
    np.save(fp, data)