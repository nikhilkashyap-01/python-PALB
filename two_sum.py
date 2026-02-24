nums = [2, 7, 11, 15]
target = 9

num_map = {}   # To store number and its index

for i in range(len(nums)):
    complement = target - nums[i]
    
    if complement in num_map:
        print([num_map[complement], i])
        break
    
    num_map[nums[i]] = i