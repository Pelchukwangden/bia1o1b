# # objective:
# create a program that takes in user input
# determine if the number is positive or negative
# print: ' ur number is positive' or "ur num is negative"
# use if else 
# print()
# input()

# 3 mins 

#break down the problem
#1. take in user input
    #  check the type of the input
    # if the type is str, how to convert it to an int?
# 2. check if the num is +ve or -ve
    #  nned to use if else statement    
    # u will be comapring nums and not str
#print the results 



userInput = input("Please type any number :")
userInputType = type(userInput)
print('the type of user input is :', userInputType)

userInputNumber = float(userInput)
print (' the type of userInputNumber is:', float(userInputNumber))

# if userInputNumber > 0:
#     print('the number is positive')
# if userInputNumber <  0:
#     print(' the number is negative')
# if userInputNumber ==  0:
#     print(' the number is zero')

if userInputNumber > 0:
    print('the number is positive')
elif userInputNumber < 0:
    print ('the number is negative')
else:
    print('the number is zero'# if a condition if true for eg the first one, the 2nd will not exicute
          

