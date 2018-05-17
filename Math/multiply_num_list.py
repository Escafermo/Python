def multiply(numbers):
    prod = 1
    for i in range(0, len(numbers)):
        prod *= numbers[i]
    return prod