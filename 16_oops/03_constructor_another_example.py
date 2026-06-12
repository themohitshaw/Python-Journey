class Dog:
    def __init__ ( self,name='Unknown', age="Notcalculated"):
        self.name = name
        self.age = age
    
    def print_info(self,color):
        self.color = color
        print(f"The name of the dog is {self.name}. Age of the dog is {self.age} and the color is {self.color}")
    

dog1 = Dog("Pawan",13)

dog1.print_info("red")