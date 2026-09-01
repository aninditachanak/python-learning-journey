import statistics

data = [10, 20, 30, 40, 50, 60, 70, 80]

q1, q2, q3 = statistics.quantiles(data, n=4)

iqr = q3 - q1

print("Data:", data)
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)
print("IQR:", iqr)
