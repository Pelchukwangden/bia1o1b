#searching 
#sorting

#prb 1
user_input = [1,2,3,4,5,6,7,8,9,11]

#check to see if the certain nums exit in the input
n = 11
print('before for loop')
for e in user_input:
    if e == n:
        print("found")
    else:
        print("not_found")

#if else, for loops, print, calculations (=,-)

n = 14

result = False
for x in user_input:
    if x == n:
        result = True

if result == True:
    print('found')
else:
    print('not found')

input =[1,2,3,4,5]
for i in input:
    print(i)
#time O(n)

input = [1,2,3,4,5]
for i in input:
    print('hi')
    if i == 1:
        break
    #O(1)

input = [1,2,3,4,5]
for i in input:
    if i == 1:
        continue
    print('hi')
    #O(n)

input = [1,2,1]
for i in input:
    for k in input:
        print('he')
        #O(n2)

input = [1,2,1]
for i in input:
    for k in input:
        for m in input:
            break
        print('dsd')
        #O(n3)

input= [1,2,3,1,2,3]
for i in input:
    #di sth
    print('hi')
for k in input:
    print('hello')
    #O(2n) != N^2

input= [1,2,3,1,2,3]
for i in input:
    #di sth
    print('hi')
    for m in input:#n^2
        print('help')
        for l in input:#n
            print('pel')
    for k in input:#n
        print('hello')
        #n^3 + n^2


#binary search 
r = False
i = [1,2,3,4,5,6,7,8,9]
#step 1 input should be sroted
#O(log N)

#1 divide by 2
#check if n is there
#check if grater of lesser
#discasrd the half






