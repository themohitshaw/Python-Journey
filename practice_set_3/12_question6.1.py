# Write a program that counts how many vowels are in a given string.

sentence = "Coding in Python is fun"
sum=0
vowels = ['a','e','i','o','u']
for char in sentence.lower():
    print(char)
    if(char in vowels):
        sum = sum+1
    

print(f"There are {sum} number of vowels in this string")