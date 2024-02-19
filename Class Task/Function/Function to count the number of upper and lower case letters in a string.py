def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Example usage
sample_string = 'The quick Brow Fox'
upper, lower = count_upper_lower(sample_string)
print("No. of Upper case characters:", upper)
print("No. of Lower case Characters:", lower)
