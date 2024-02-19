# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the common elements between set1 and set2
common_elements = set1.intersection(set2)

# Update set1 to contain only the common elements
set1.intersection_update(set2)

# Print the updated set1
print("Updated set1:", set1)
