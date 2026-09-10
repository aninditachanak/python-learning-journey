from scipy.stats import f_oneway

group_a = [10, 12, 11, 13, 12]
group_b = [20, 22, 21, 23, 22]
group_c = [30, 32, 31, 33, 32]

f_value, p_value = f_oneway(group_a, group_b, group_c)

print("F-value:", f_value)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null Hypothesis")
