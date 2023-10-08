letter ='''Dear <|Name|>,
Greeting from ABC company .
You are selected!
Date: <|Date|
'''
name = input("enter your name\n")
date = input("enter Date\n")
letter=letter.replace("<NAME|>",name)
letter=letter.replace("<DATE|>", date)
print(letter)