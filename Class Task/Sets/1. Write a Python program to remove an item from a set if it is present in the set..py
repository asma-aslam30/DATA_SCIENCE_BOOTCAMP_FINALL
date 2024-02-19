# Define a set
my_set = {3, 6, 9, 12, 15}

# Item to remove
item_to_remove = 9

# Check if the item is present in the set
if item_to_remove in my_set:
    # Remove the item from the set
    my_set.remove(item_to_remove)
    print(f"{item_to_remove} removed from the set.")
else:
    print(f"{item_to_remove} is not present in the set.")

# Print the updated set
print("Updated Set:", my_set)
