# Define the set
set1 = {10, 20, 30, 40, 50}

# Items to remove
items_to_remove = {10, 20, 30}

# Remove items from the set using discard() method
for item in items_to_remove:
    set1.discard(item)

# Print the updated set
print("Updated Set:", set1)
