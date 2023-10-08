with open("log.txt") as f:
    content = f.read().lower()

if 'python ' in content:
    print("Yes python is available")    
else:
    print("No python is available")    