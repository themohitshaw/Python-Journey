marks = [1,2,3,1,1,4,6]
print(marks)

marks.append(5) #Adding an element to the list and it will change the original string
print(marks) #Lists are mutable 

marks.pop() # It will remove the last item in the list
marks.pop(2)# It will remove the  item which is in the index 2 of the list 
print(marks)

marks.insert(1,7) #It add the element at the given index for example 7 1t index 1 in marks list
print(marks)

extra_marks = [10,11,12]
marks.extend(extra_marks) #It add the item of  an another list to a list
print(marks)

marks.remove(10) #It will remove a item from the list
print(marks)

marks.reverse() #It will reverse the items in a list
print(marks)

marks.sort() #It will sort the items in  a list
print(marks)

# marks.clear()#It clear all the items from the list
# print(marks)

copy_marks = marks.copy() #It create a copy of original list
print(copy_marks)

total_element = marks.count(1) #It counts the item repetation
print(total_element)

