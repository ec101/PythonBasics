def celsiusToFarenheit(celsius):
    if(celsius < -237.15):
        return "Too Low"
    else:
        return celsius * 9 / 5 + 32


temperatures = [10, -20, -289, 100]

with open("temps.txt", "w") as file:
    for temp in temperatures:
        val = celsiusToFarenheit(temp)
        if float == type(val):
            file.write(str(val)+"\n")