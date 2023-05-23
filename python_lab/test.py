def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            #max_num += num
            #num = max_num
            #max_num += num
            max_num = num 
    print(max_num)
    return max_num

a = find_max([3])
print(a)