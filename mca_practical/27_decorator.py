def smart_div(func):
    def inner(a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return func(a, b)

    return inner


@smart_div
def div(a, b):
    return a / b


# Example usage
result1 = div(10, 2)
print("Result 1:", result1)

result2 = div(5, 3)
print("Result 2:", result2)
