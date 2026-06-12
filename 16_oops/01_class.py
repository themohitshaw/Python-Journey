# Class : Class is a blueprint or template. Eg a Form for a exam that contain name, age , electives and father's name etc

# Object : Specific instance created from the template (Class.). Eg Form which contains the data of John Deo

class employee:
    company = "HP"

    def get_salary(self):   #Self is important here because self is a way to reference the object of the class which is being created
        print(self)
        return 34000
    


e1 = employee()  #An object of class employee created here
print(e1.get_salary())  # Employee e1's get_salary method is called
print(e1.company)

e2  = employee()
print(e2.get_salary())
print(e2.company)