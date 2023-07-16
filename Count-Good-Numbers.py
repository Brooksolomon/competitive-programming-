class Solution:
    def countGoodNumbers(self, n: int) -> int:
        numofeven=5
        numofprime=4
        def helper(m,n):
            if n==0:
                return 1
            if n< 0 :
                return 1/ helper(m,-n)
            if n%2 == 0:
                return helper((m**2) % (10**9 + 7) , n//2)
            else:
                return m*helper((m*m) % (10**9 + 7), (n-1) // 2)
            
        evenoutcome =  helper(numofeven,(n//2 + n%2)) % (10**9 + 7)
        oddoutcome = helper(numofprime,n//2)  % (10**9 + 7)
        return (evenoutcome*oddoutcome) % (10**9 + 7)
