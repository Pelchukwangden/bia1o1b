#we use while loop unilt condition are met
#return true or fALSE
# it keeps on running until the conditon is true

count = 0
while count < 1:
    print(count)
    count = count + 1 #output 0 1 2 3 4 

#user input str is unknown
#counter --
p = "peldenwangchuk"
counter = 0
lenght_of_p = len(p)
print("counter is :", counter)
print("lenght_of_p :", lenght_of_p)

print('going in loop')
while counter < lenght_of_p:
    print("counter:", counter)
    char = p[counter]
    print(char)
    counter = counter + 1 #output p, e, l ,d.........


p = "peldenwangchuk"
counter = 0
lenght_of_p = len(p)
print("counter is :", counter)
print("lenght_of_p :", lenght_of_p)

print('going in loop')
while counter < lenght_of_p:
    print("counter:", counter)
    char = p[counter]
    print(char)
    counter = counter + 1
    print("-------")


