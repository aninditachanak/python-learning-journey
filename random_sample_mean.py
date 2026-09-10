import random

data = [10, 20, 30, 40, 50, 60, 70, 80]

sample = random.sample(data, 4)

mean = sum(sample) / len(sample)

print("Original Data:", data)
print("Random Sample:", sample)
print("Sample Mean:", mean)
