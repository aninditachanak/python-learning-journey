from scipy.stats import skew

data = [10, 20, 20, 30, 40, 50, 60]

result = skew(data)

print("Data:", data)
print("Skewness:", result)
