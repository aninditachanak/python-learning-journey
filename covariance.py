import numpy as np

X = [10, 20, 30, 40, 50]
Y = [15, 25, 35, 45, 55]

covariance = np.cov(X, Y)[0][1]

print("X:", X)
print("Y:", Y)
print("Covariance:", covariance)
