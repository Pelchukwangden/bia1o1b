input_arr = [ 6,8,3,1,5,0]

def bubble_sort(arr):#function  
    x = len(arr)

    print('before for loop')
    for i in range(x):#0,1,2,3,4,5
        print('inside first loop')
        for j in range(0, (x-1)):
            print('inside second for loop')
            element = arr[j]
            elementright = arr[j+1]
            print ('element:', element)
            print ('elementright:', elementright)
            print('======')

            #swaping
            if element > elementright:
                arr[j] = elementright
                arr[j+1] = element
                print('swapped:', arr)
    print('final arr:', arr)
bubble_sort(input_arr)


