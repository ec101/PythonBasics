numbers = [1,2,3]

file = open("numbers.txt", "w")

for i in numbers:
    file.write(str(i)+"\n")
    
file.close()

file = open("numbers.txt", "a")
file.write(str(4))
file.close()
