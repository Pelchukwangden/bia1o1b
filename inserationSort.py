input_arr = [6,3,1,5,0]


def insertation_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1 #compare the cuttrent element wiht thel left elements

    #this loop is for comntionously comparing the 
    #the current element wiht the left elemenet unit it is on the correct sport
        while j >= 0 and key < arr[j]:
            #swaP
            arr[j+1] = arr[j]
            j -= 1 #if current element is less then the left 
        arr[j+1] = key
    return arr

sortedarr = insertation_sort(input_arr)
print(sortedarr)
