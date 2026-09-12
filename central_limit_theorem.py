import numpy as np

population = np.arange(1, 101)

sample_means = []

for i in range(100):
    sample = np.random.choice(population, 10)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
