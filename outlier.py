numbers = [10, 12, 15, 14, 13, 12, 16, 100, 11, 14]

numbers.sort()

n = len(numbers)

# Find Q1 and Q3
q1 = numbers[n // 4]
q3 = numbers[(3 * n) // 4]

# Calculate IQR
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = []

for num in numbers:
    if num < lower_limit or num > upper_limit:
        outliers.append(num)

print("Numbers:", numbers)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Outliers:", outliers)
