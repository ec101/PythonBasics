import datetime

fileNames = ["file1.txt", "file2.txt", "file3.txt"]

content = []

for fileName in fileNames:
    with open(fileName, "r") as file:
        content = content + file.readlines()

outputFileName = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

with open(outputFileName, "w") as mergeFile:
    for item in content:
        mergeFile.write(item + "\n")