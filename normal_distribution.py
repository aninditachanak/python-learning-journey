import numpy as np

data = np.random.normal(50, 10, 10)

mean = np.mean(data)
std_dev = np.std(data)

print("Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
