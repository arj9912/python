myDict ={
    "panka": "fan",
    "dabba": "box",
    "vastu": "Iteam"

}
print("Options are",myDict.keys())
a = input ("Enter the nepali Word\n")
# print("the meaning of your word is :",myDict[a])
# below line will not throw an error if the key is not present in the dictionary
print("the meaning of your word is :",myDict.get(a))
