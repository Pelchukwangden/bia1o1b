#sth repetative
#write a logic and call it when ever u want

def greet():
    #do some calculation code
    #complex stuffs
    print("hello there")#u have just give him the code didnt run
#u write a code and put in function and u can run when u want
greet()

def greet_pala():
    print("hello boss")

user_input ="dorji"

if user_input == "pala":
    greet_pala()

user_input = "pala"

if user_input == "pala":
    greet_pala()


def add_nums(num1, num2):
    sum = num1 + num2
    print("adding number")
    print(sum)
    #if is said the he will reveive 2 values num1 and 2

user_num1 = 10
user_num2 = 20

add_nums(user_num1, user_num2)
#OR USE
add_nums(10,20)

#returning the value
def add_nums(num1, num2):
    sum = num1 + num2
    print("adding number")
    # print(sum)
    return sum

user_num1 = 1
user_num2 = 6

return_sum = add_nums(user_num1, user_num2)
print(return_sum)
