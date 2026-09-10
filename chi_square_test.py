from scipy.stats import chisquare

observed = [20, 30, 50]
expected = [25, 25, 50]

chi_square, p_value = chisquare(observed, f_exp=expected)

print("Chi-Square Value:", chi_square)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Accept the Null Hypothesis")
