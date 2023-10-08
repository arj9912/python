def remove_and_split(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "    Arjun is a good"
n = remove_and_split(this,"Arjun")
print(n)