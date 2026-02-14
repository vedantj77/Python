# lists in python contain of diff types of elements ex. int, string and can change value (mutable)
nums = [12,22,33,44,1000,231]
#nums.insert(this is the position where we want to insert,this is what we want to insert)
nums.insert(3,27)
#nums.pop() it will pop/remove the last element OR nums.pop(index value)
nums.pop()
#nums.remove(22) used to remove elements using specific values
nums.remove(44)
#nums.append() used to add elements at the last
nums.append(999)
#nums.extend extends the list
nums.extend([989,288,2212])
#sorts in ascending
nums.sort()
#Lists are muteable
nums[0] = 99
print(nums)


l = [1,2,3,4,5,6]

l.append([7,8])
print(l)
print(l[6])
l.pop(2)
print(l)

heros=['redranger','mystic',23,22,44,33]
print(heros)