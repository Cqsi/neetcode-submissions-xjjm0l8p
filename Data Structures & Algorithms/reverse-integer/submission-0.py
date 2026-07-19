class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648
        MAX = 2147483648

        # we have to be careful with neg. numbers
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x:

            digit = x%10
            x //= 10

            if res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10):
                return 0
            
            res = (res*10) + digit

        res *= sign
        return res