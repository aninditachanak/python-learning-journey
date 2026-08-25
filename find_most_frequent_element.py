numbers = [10, 20, 30, 20, 40, 20, 50, 30, 20]

most_frequent = numbers[0]
max_count = 0

for num in numbers:
    count = numbers.count(num)

    if count > max_count:
        max_count = count
        most_frequent = num

print("List:", numbers)
print("Most frequent element:", most_frequent)
print("Frequency:", max_count)
