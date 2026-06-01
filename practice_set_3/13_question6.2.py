# Take a user input string and check if it is a palindrome (same forwards and
# backwards).

str = input('Enter a string: ')
print(f"You entered the string: {str}")

r_str = str[::-1]

if(str == r_str):
    print("This string is palindrome")
else:
    print("This string is not palindrome")
