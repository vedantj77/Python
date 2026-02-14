nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    hash_map={}

    for i,x in enumerate(nums):
        if target - x in hash_map:
            return[hash_map[target-x],i]
        hash_map[x] = i
    return []

print(twoSum(nums, target))