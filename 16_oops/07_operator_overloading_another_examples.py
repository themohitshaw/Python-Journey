#Another example for points
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self,another_point):
        if((self.x == another_point.x) and(self.y == another_point.y)):
            return "Equal"
        else:
            return "Not equal"
    


p1 = point(3,4)
p2 = point(3,6)

res_point = p1.__eq__(p2)
print(res_point)

print(p1 == p2)


#Another_Example for List

class list_example:
    def __init__(self,my_list):
        self.my_list = my_list
    
    def __getitem__(self, key):
        print(self.my_list[key])
    
    def __setitem__(self, key, value):
        self.my_list[key] = value
        print(self.my_list)
    
    # def __delitem__(self, key):
    #     self.my_list.remove(key)
    #     print(self.my_list)

    #Or

    def __delitem__(self, key):
        del self.my_list[key]
        print(self.my_list)


list1 = [1,2,3,4,5]

obj1 = list_example(list1)
# obj1.__getitem__(3)
# obj1.__setitem__(2,4)
# obj1.__delitem__(2)

obj1[3]
obj1[4]=3
del obj1[2]


#Another example for Dictionary

class dictionary_example:
    def __init__(self,my_dict):
        self.my_dict = my_dict

    def __getitem__(self, key):
        return self.my_dict[key]
    
    def __setitem__(self,key,value):
        self.my_dict[key] = value
        print(self.my_dict)
    
    # def __delitem__(self, key):
    #     self.my_dict.pop (key)
    #     print(self.my_dict)
    
    def __delitem__(self, key):
        del self.my_dict[key]
        print(self.my_dict)
    

    


obj1 = dictionary_example({"Harry":50 , "John":35 , "Rony":13})
print(obj1["Harry"])

obj1["John"]=45

del obj1["John"]

del obj1["Rony"]

# Another examples for numbers

class number_example:
    def __init__(self,a):
        self.a = a
    
    def __add__(self,another_number):
        return (self.a + another_number.a)
    
    def __sub__(self,another_number):
         return (self.a - another_number.a)
    
    def __mul__(self,another_number):
        return (self.a * another_number.a)
    
    def __truediv__(self,another_number):
        return (self.a / another_number.a)
    
    def __eq__(self, another_number):
        if(self.a == another_number.a):
            print('Equal')
        else:
            print('Not equal')

    def __ne__(self, another_number):
        if(self.a != another_number.a) :
            print('Right')
        else:
            print('Wrong')   
        
    def __le__(self,another_number):
        if(self.a <= another_number.a):
            print("Right")
        else:
            print("Wrong")

    def __ge__(self,another_number):
        if(self.a >= another_number.a):
            print("Right")
        else:
            print("Wrong")
    


n1 = number_example(4)
n2 = number_example(3)

add = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2
print(add , sub , mul , div,sep=",")

n1 == n2
n1!=n2
n1 <= n2
n1 >= n2

#Another Example for string

class string_example:
    def __init__(self,my_string):
        self.my_string = my_string
    
    def __len__(self):
        return len(self.my_string)

s = string_example("Code With Harry")

# length = len(s)
# print(length)

#or

print(len(s))
