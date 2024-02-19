# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find the common elements using the intersection() method
common_elements = set1.intersection(set2)

# Check if there are any common elements
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found.")
