content = True
i =1
with open("log.txt") as f:
    while content:
       content = f.readline()

    if 'python ' in content.lower():
        print(content)
        print(f"Yes python is available number {i}")  
        print(i)  
        i+=1
