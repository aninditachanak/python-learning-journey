import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

percentile_25 = np.percentile(data, 25)
percentile_50 = np.percentile(data, 50)
percentile_75 = np.percentile(data, 75)

print("Data:", data)
print("25th Percentile:", percentile_25)
print("50th Percentile:", percentile_50)
print("75th Percentile:", percentile_75)
