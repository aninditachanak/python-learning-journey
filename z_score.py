import statistics

data = [10, 20, 30, 40, 50]

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print("Data:", data)
print("Mean:", mean)
print("Standard Deviation:", std_dev)

for x in data:
    z = (x - mean) / std_dev
    print("Z-score of", x, "=", round(z, 2))
