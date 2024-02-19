# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find the items in set2 that are not present in set1
items_to_add = set2.difference(set1)

# Update set1 by adding items from set2, except common items
set1.update(items_to_add)

# Print the updated set1
print("Updated set1:", set1)
