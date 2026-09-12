X = [10, 20, 30, 40, 50]
Y = [15, 25, 35, 45, 55]

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

total = 0

for i in range(len(X)):
    total += (X[i] - mean_x) * (Y[i] - mean_y)

covariance = total / (len(X) - 1)

print("Mean of X:", mean_x)
print("Mean of Y:", mean_y)
print("Covariance:", covariance)
