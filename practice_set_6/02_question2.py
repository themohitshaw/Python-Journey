'''
2. Constructor and Attributes
Create a class Person with a constructor ( __init__ ) that accepts name and age
as arguments and stores them as instance attributes.
Create an object and print the person’s name and age.

'''

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def person_info(self):
        print(f"My name is {self.name} and i am {self.age} years")
    

p1 = person("John Deo",24)
print(p1.name)
print(p1.age)

p1.person_info()