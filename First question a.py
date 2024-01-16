#Input the string “Python” as a list of characters from console, delete at least 2 characters, reverse the resultantstring and print it.

# Enter the string 'Python' as a list of characters
input_string = list(input("Enter the string 'Python': "))

# Deleting at least 2 characters
if len(input_string) >= 2:
    del input_string[:2]
else:
    print("Cannot delete less than 2 characters.")

# Reversing the resultant string
resultant_string = input_string[::-1]

# Printing the reversed string
print("Reversed String:", ''.join(resultant_string))
