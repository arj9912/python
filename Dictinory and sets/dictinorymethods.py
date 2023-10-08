myDict ={
    "fast": "In a Quick Manner",
    "arjun":"A Colder",
    "Marks":[1,2,3],
    "anotherdict":{'arjun':'Player'},
    1:2
}

# print(myDict.keys())
# print(list(myDict.keys())) #prints the keys of the dictionary
# print(myDict.values()) # prints the keys of the dictionary

print(myDict.items()) # prints the (keys, values) for all contents of the dictionary
print(myDict)
updateDict ={
    "lovish": "Frinds",
    "hari": "Frinds",
}
myDict.update(updateDict) # updates dthe dictionary by adding key-values pairs from updateDict
print(myDict)

print(myDict.get("arjun")) # prints value associated with key "arjun"
print(myDict["arjun"]) # prints value associated with key "arjun

# the difference between .get and []syntax in dictionary?
print(myDict.get("arjun2")) # returns none as arjun2 is not present in the dictionary
print(myDict["arjun2"]) # throws an error a arjun2 is not present in the dictionary