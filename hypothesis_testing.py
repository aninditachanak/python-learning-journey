from scipy.stats import ttest_1samp

sample = [22, 25, 28, 24, 26, 27, 23, 25]
population_mean = 25

t_stat, p_value = ttest_1samp(sample, population_mean)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null Hypothesis")
