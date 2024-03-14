result = ""
nameTest = "Pelden"
for x in nameTest:
    if x == "P":
        result += "1"
    elif x == "e":
        result += "2"
    elif x == "l":
        result += "3"
    elif x == "d":
        result += "4"
    elif x == "n":
        result += "5"
    else:
        result = result + x

print (result)

