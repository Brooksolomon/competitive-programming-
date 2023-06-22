class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans=[]
        def pas(n):
            cur = [1] * n
            for i in range(1,n-1):
                cur[i] = ans[n-2][i-1] + ans[n-2][i]
            ans.append(cur)
            if n==rowIndex+1:return
            else:pas(n+1)  
        pas(1) 
        return ans[rowIndex]
