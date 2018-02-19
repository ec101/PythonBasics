file = open("fruits.txt")
content = file.readlines()
file.close()

for i in content:
    print(len(i.strip()))
