class Solution:
    def isHappy(self, n: int) -> bool:

        def hsum(num):
            digit = 0
            sum = 0
            while num > 0:
                digit = num % 10
                sum += digit **2
                num = num//10
            return sum 

        seen = set()
        while hsum(n) not in seen:
            sum1 = hsum(n)
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1
        return False
                