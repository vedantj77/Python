class Solution(object):
    def missingNumber(self,array):
        n=len(array)

        expected_sum = n * (n+1) // 2
        summ = sum(array)
        return expected_sum - summ
