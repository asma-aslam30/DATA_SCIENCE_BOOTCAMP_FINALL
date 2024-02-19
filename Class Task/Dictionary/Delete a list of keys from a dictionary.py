# Define the sample dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

# Keys to remove
keys_to_remove = ["name", "salary"]

# Remove keys from the dictionary using a loop
for key in keys_to_remove:
    if key in sample_dict:
        del sample_dict[key]

# Print the modified dictionary
print("Modified Dictionary:", sample_dict)
