import numpy as np

data = [10, 12, 14, 15, 18, 20, 22, 25, 100]

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = []

for x in data:
    if x < lower_limit or x > upper_limit:
        outliers.append(x)

print("Outliers:", outliers)
