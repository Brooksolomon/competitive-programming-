class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x=0
        ans=[]
        for i in range(int(sqrt(c)) + 1):
            ans.append(x*x)
            x+=1
        left=0
        right=len(ans) -1
        for i in range(len(ans)):
            if ans[left] + ans[right] == c:
                return True
            elif ans[left] + ans[right] > c:
                right-=1
            else:left+=1
        return False 
