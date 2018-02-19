def stringLength(string):
    tpe = type(string).__name__
    if "int" in tpe:
        print("Sorry integers don't have length")
        return 0
    elif "float" in tpe:
        print("Sorry floats don't have length")
        return 0
    else:
        return len(string)
        
#print(type(10))
print(stringLength(10.0))