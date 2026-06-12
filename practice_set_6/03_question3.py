'''
3. Simple Inheritance
Create a base class Animal with a method sound() that prints "Some sound" .
Create a derived class Dog that overrides sound() to print "Bark!" .
Create an object of Dog and call sound() .
'''

class animal:
    def sound(self):
        print("Some sound!!")
    
class dog(animal):
    def sound(self):
        super().sound()
        print("Bark!!")


d1 = dog()
d1.sound()
