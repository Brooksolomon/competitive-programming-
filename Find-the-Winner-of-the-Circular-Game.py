class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p=0
        a =[i for i in range(1,n+1)]
        for i in range(n-1):
            p=(p+k -1) % (n-i)
            a.pop(p)
        return a[0]
            
