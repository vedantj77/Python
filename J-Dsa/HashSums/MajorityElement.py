from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        javl = 0
        maxcount = 0

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

            # Check if this num has the highest frequency so far
            if count[num] > maxcount:
                javl = num
                maxcount = count[num]

        return javl

nums = [2, 2, 1, 1, 1, 2, 2]
