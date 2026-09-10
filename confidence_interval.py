import statistics
from scipy.stats import t

data = [10, 12, 14, 15, 18, 20, 22, 25]

mean = statistics.mean(data)
std_dev = statistics.stdev(data)
n = len(data)

# 95% confidence interval
confidence = 0.95
alpha = 1 - confidence

t_value = t.ppf(1 - alpha / 2, n - 1)

margin_error = t_value * (std_dev / (n ** 0.5))

lower = mean - margin_error
upper = mean + margin_error

print("Mean:", mean)
print("95% Confidence Interval:")
print("Lower Limit:", lower)
print("Upper Limit:", upper)
