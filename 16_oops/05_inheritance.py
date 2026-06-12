class animal:
    location = "Austrelia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking Now")

class dog(animal):  # This is how inheritance is done in python
    def speak(self):
        super().speak()  #We are using the speak function of the parent class
        print("woof")


# a = animal("Dog")
# a.speak()

d = dog("Bruno")
d.speak()
print(d.location)

d1= dog("Rony")
print(d.location)