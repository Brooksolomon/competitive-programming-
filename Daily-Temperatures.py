class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans=[]
        ans.append(0)
        new=[]
        for i,e in enumerate(temperatures):
            new.append((e,i))
        stack=[]
        stack.append(new[-1])
        for i in range(len(temperatures)-2,-1,-1):
            while stack:
                if new[i][0] >= stack[-1][0]:
                    stack.pop()
                else:
                    ans.append(stack[-1][1]-i)
                    break
            else:ans.append(0)
            stack.append(new[i])
        return ans[::-1]
