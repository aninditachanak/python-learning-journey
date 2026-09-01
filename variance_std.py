import math

data = [10, 20, 30, 40, 50]

mean = sum(data) / len(data)

squared_sum = 0

for x in data:
    squared_sum += (x - mean) ** 2

variance = squared_sum / (len(data) - 1)

standard_deviation = math.sqrt(variance)

print("Data:", data)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
