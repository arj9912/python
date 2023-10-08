# Creating  an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not change the
b.add((4,5,6))
# b.add({4:5})# Cannot add list or dictionary to sets
print(b)
# length of the set
# print(len(b)) # prints the length of this set

# removal of an element
# b.remove(5) #  Remove 5 from set b
# b.remove(15) # throws an error while trying to remove 15(which is not present in the set)
# print(b)

print(b.pop())
