from scipy.stats import linregress

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

result = linregress(X, Y)

print("Slope:", result.slope)
print("Intercept:", result.intercept)
print("Correlation Coefficient:", result.rvalue)
print("R-squared:", result.rvalue ** 2)
