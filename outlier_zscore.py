import statistics

data = [10, 12, 14, 15, 18, 20, 22, 25, 100]

mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print("Mean:", mean)
print("Standard Deviation:", std_dev)

outliers = []

for x in data:
    z = (x - mean) / std_dev

    print("Value:", x, "Z-score:", round(z, 2))

    if abs(z) > 2:
        outliers.append(x)

print("Outliers:", outliers)
