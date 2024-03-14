#array, dtacks, ques, dict
#differe by how they store data
#ARRAY can store multiple data --can instert elemnt in any positon
#STACK (can only add or pop)-- 
#QUES first in first out  
#DICT/HASHMAP is a key and value player 


#creation of array 
array1 = [1,2,3,"thimphu", 2.5]#can store any data type

#retriving the data
element1 = array1[0]
element4 = array1[4]
print (element4)

#modifying emelment withoin the array 
array1[0] = 10
print(array1)

#how many elemnt in array
no_of_element = len(array1)
print(no_of_element)

#negative indexing 
last_element = array1[-1]
print(last_element)

last_element = array1[-5]
print(last_element)

#retrive certain len of array(slicing)
elements = array1[0:2]#the element in 2 index wont be print 
print(elements)

#concatenation of lists
list1 = [1,2,3]
list2 = [4,5,6]
new_list = list1 + list2#how u order matters 
print(new_list)

#check if the num is in the list or not
list1 = [1,2,3]
list2 = [4,5,6]
number_to_check = 2
result=number_to_check in list1
result1=number_to_check in list2
print(result)
print (result1)#str "2" != 2

#add in the list 
a = [1,2,3]
a.append(4)
print(a)

#insert in a specifie place
a = [1,2,3]
a.insert(1,10)
print(a)

#sort
a.sort()
print(a)

#STACK
stack = []

#Adding in stack
stack.append(4)
stack.append(2)
stack.append(9)
stack.append(1)#4, 2 ,9, 1

#removing from stack
stack.pop()
print('after poping', stack)


#adding the removed item in another 
element = stack.pop()
print('removed element:', element)


