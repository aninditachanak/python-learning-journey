import numpy as np

n = 10
p = 0.5

data = np.random.binomial(n, p, 10)

print("Number of heads in each experiment:")
print(data)
