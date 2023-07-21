class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right  = 0 , num

        while left <=right:
            m = left + (right-left) // 2

            if m*m == num:return True
            elif m*m < num:left = m+1
            else: right = m-1
        return False
