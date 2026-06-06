marks = {"Harry":32 , "Jack":45 , "Lily":93}

print(marks.keys()) #It return all the keys of the dictionary

print(marks.values()) #It return all the values of the dictionary

print(marks.items()) #It returns all the items of the dictionary

# marks.clear()  #It clear all theitems from the dictionary
print(marks)

marks.pop("Lily") #It clear the key from the dictionary
print(marks)

marks_copy = marks.copy() #It create a copy of the original dictionary
print(marks_copy)

key = ["Mohit","Rahul","Priya"]
attendance = dict.fromkeys(key)
print(attendance)

print(marks.get("Harry"))  #It returns the value of the given key

marks.popitem() #removes and returns the last inserted key-value pair from a dictionary.
print(marks)

marks.setdefault("Ranjan",30) #setdefault() is a dictionary method that does two things in one step:
# Checks if a key exists in the dictionary
# If not, inserts the key with a default value
print(marks)

marks.update({"Ranjan":45 , "Harry":14})  #method is used to add new key-value pairs or update existing key-value pairs in a dictionary.
print(marks)




