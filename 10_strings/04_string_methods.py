s = "hello world" # Strings are immutable

# s[0] = "R" # You can not do this

a = len(s)
print(a)

print(s.upper(), s)
print(s.lower(), s)
print(s.capitalize(), s)
print(s.title(), s)

# Removing Whitespace
text = "  hello world  "
print(text.strip()) # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"

# Finding and Replacing
text = "Python is fun"
print(text.find("is")) # Output: 7 find the first occurence
print(text.replace("fun", "awesome")) # Output: "Python is awesome

# Splitting and Joining
text = "apple,banana,orange"
fruits = text.split(",")
print(fruits) # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text) # Output: "apple - banana - orange"

# Checking String Properties
text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False
