# Accept string input from user
input_string = input("Enter a string: ")

# Capitalize the first character of each word
capitalized_string = ' '.join(word.capitalize() for word in input_string.split())

# Display the capitalized string
print("Capitalized String:", capitalized_string)
