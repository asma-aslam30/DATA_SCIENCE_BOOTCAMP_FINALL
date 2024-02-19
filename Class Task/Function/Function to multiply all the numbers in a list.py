def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
sample_list = [8, 2, 3, -1, 7]
print("Multiplication of numbers in the list:", multiply_list(sample_list))

