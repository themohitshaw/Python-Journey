# Using format() , create a sentence:
# "My name is John and I am 25 years old."
# by passing "John" and 25 as variables.

template = "My name is {} and I am {} years old."
name = "John"
age = 25

s = template.format(name,age)
print(s)

