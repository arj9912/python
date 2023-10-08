# n! = 1 X 2X 3X 4X 5X 6X 

num = int(input("Enter the number\n"))

factorial = 1
for i  in range(1, num+1):
    factorial = factorial*i

print(f"yhe factorial of {num} is {factorial}")    