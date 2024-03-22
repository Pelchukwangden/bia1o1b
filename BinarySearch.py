arr = [3,4,5,6,7,8,9]
target = 7

low = 0
high = len(arr)-1

while low <= high:
    #divide
    mid = (low + high)//2
#    print('mid:', mid)
#     print('low:', low)
#     print('high:', high)
#     print('---------') 

    #compare the middle with the taget
    if arr[mid] == target:
        print('found')
        break

    #compare and discard the half
    if target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1


arr = [3,4,5,6,7,8,9]
target = 9

low = 0
high = len(arr)-1

result = False

while low <= high:
    #divide
    mid = (low + high)//2
#    print('mid:', mid)
#     print('low:', low)
#     print('high:', high)
#     print('---------') 

    #compare the middle with the taget
    if arr[mid] == target:
        result = True
        print('found')
        break

    #compare and discard the half
    if target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1

if result == True:
    print('found')
else:
    print('not found')