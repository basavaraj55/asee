# stats_processor.py

numbers = [12, 45, 7, 89, 34, 23, 67, 3, 90, 21]

total = sum(numbers)
count = len(numbers)
average = total / count
maximum = max(numbers)
minimum = min(numbers)

sorted_numbers = sorted(numbers)

print("Original Numbers:", numbers)
print("Sorted Numbers:", sorted_numbers)
print("Total:", total)
print("Average:", round(average, 2))
print("Max:", maximum)
print("Min:", minimum)
