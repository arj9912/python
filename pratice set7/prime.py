num = int(input("Enter the number\n"))
prime = True 
for i in range(2,num):
    if (num%1==0 ):
        prime = True
        break
if prime:    
    print("this number is prime")
else:
    print("this number is not prime")    