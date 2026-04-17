# Multiplication Table

n = 5  # you can change this number

for row in range(1, n + 1):
    for col in range(1, n + 1):
        print(row * col, end=" ")
    print()
