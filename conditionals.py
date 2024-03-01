# obj: a calculator application 

#STEPS
#1. get input from the user
# do claculation based on user input
#check the type of usertypes
#if users str is * do multiplication
#give output to the user

userInput = ""

print('* for multiplication')
print("+ for addition")
print("- for subtraction")
print('/ for division')
WhatUserTypes = input()

print('User typed:', WhatUserTypes)
print("user input type", type(WhatUserTypes))

print('--------------------------')
if WhatUserTypes == "+":
    print("doing addtion")
    if "a" == 'b':
        print (' a is not b')
    if 'b' == 'b':
        print('b is b')
print("doing more addition")#level of indentations

if WhatUserTypes == "-":
    print("doing subtraction")
    print("doing more subtraction")
    