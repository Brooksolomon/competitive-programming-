class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):  
            if n==0:
                return 1
            if n < 0:
                x=1/x
                n=-n
            result = power(x,n//2)
            if n % 2 == 0:
                return result * result
            else:
                return result * result * x

        ans = power(x,n)
        return ans
