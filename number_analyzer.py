# Number Analyzer

numbers = [3, 7, 10, 15, 22]

even_count = 0
odd_count = 0
total = 0

for num in numbers:
    total += num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / len(numbers)

print("Total:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
