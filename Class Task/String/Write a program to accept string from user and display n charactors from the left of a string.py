# Accept string input from user
input_string = input("Enter a string: ")

# Accept the number of characters to display
n = int(input("Enter the number of characters to display: "))

# Display the first n characters of the string
print("First", n, "characters:", input_string[:n])
