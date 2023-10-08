# n = 4

# for i in range(4):
#     print("*" * (i+1))

n=3
for i in range(3):
    # for j1 in range(n-i-1):
        print(" " *(n-i-1), end ="")
        print(" *" *(2*i+1) , end="")
        print(" " *(n-i-1))