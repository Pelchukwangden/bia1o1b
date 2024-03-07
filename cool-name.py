#a - 4
#l - 1
#e - 3
#s - 5
#o - 0
#g - 9
#t - 7
#z - 2

#use if else statement

# dechen -D3ch3n
# hello - h3ll0
# tshewang - 75h3w4n9

#loops
# testName  = "tshewang"

# for char in testName:
#     print(char)

#replace the characters
result = ""
testName = "Tshewang"
for char in testName:
    if char == "A":
        result += "4"
    elif char == "o":
        result += "0"
    elif char == "e":
        result += "3"
    elif char == "l":
        result += "1"
    elif char == "s":
        result += "5"
    elif char == "g":
        result += "9"
    elif char == "b":
        result += "6"
    elif char == "t":
        result += "7"
    elif char == "z":
        result += "2"
    else:
        result = result + char

    print (result)

#task 