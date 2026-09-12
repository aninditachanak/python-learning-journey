from scipy.stats import kurtosis

data = [10, 20, 20, 30, 40, 50, 60]

result = kurtosis(data)

print("Data:", data)
print("Kurtosis:", result)
