input_arr = [1,2,3,4,1]

def containsDuplicate(nums):
    #solution code here
    for index1 in range(0, len(nums)):
        for index2 in range(0, len(nums)):
            if index1 == index2:
                continue
            # print('i1:', index1)
            # print('i2:', index2)
            value1 = nums[index1]
            value2 = nums[index2]
            # print('val1:', value1)
            # print('val2:', value2)
            # print('================')
            if value1 == value2:
                return True

        return False
    #retrun true or false

result = containsDuplicate(input_arr)
print(result)