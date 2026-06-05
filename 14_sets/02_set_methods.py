s = {1,2,3,4,5}
print(s)

s.add(32)
print(s)

s.remove(2)
print(s)

# s.remove(4434)  #It throw a error because this item (4434) is not present at the set 

s.discard(4434) #It remove the item only if the item exists in the set otherwise it silent
print(s)

s.pop() #It removes random element from the set
print(s)