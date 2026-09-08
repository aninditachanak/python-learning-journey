import numpy as np
from scipy.stats import linregress

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

result = linregress(X, Y)

slope = result.slope
intercept = result.intercept

print("Slope:", slope)
print("Intercept:", intercept)

# Predict Y when X = 6
x = 6
y = slope * x + intercept

print("Predicted value when X =", x, ":", y)
