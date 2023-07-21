class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0 , x

        while left <=right:
            m = left+ (right - left) //2
            if m*m < x:
                left = m  + 1
            elif m*m > x:
                right = m - 1
            else:
                return m
        return right
