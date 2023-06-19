def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2
a = 1  # Starting number
b = 5  # Ending number

for square in squares(a, b):
    print(square)
