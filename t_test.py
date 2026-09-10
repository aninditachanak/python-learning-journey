from scipy.stats import ttest_ind

group_a = [20, 22, 21, 23, 24]
group_b = [25, 27, 26, 28, 29]

t_stat, p_value = ttest_ind(group_a, group_b)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("The means are significantly different")
else:
    print("The means are not significantly different")
