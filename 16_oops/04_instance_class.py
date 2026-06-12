class employee:

    company = "Asus" #This is class attribute
    def __init__(self,salary,name,bond,company):
        self.company = company
        self.salary = salary  #Create a instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
    

e1 = employee(34000,"John",4,"Tesla")
print(e1.company) #Will always print instance attribute  whenever present
print(employee.company) #Will always print class attribute whenever present

#Object introspection - It is a way to find all the methods and attributes of a particular object in python

print(dir(e1))

