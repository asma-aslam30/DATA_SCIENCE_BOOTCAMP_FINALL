# Define the dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine the dictionaries by adding values for common keys
combined_dict = {}
for key in d1.keys() | d2.keys():
    combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

# Print the combined dictionary
print("Combined Dictionary:", combined_dict)
