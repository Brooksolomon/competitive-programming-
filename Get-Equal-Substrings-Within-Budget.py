class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        pr=[]
        for i in range(len(s)):
            pr.append(abs(ord(s[i]) - ord(t[i])))
        print(pr)
        left = 0
        right = 0
        summer = 0
        maxl = 0
        while right < len(pr):
            summer+=pr[right]
            if summer>maxCost:
                while left < len(pr) and summer > maxCost:
                    summer-=pr[left]
                    left+=1
            else:
                maxl=max(maxl,right-left+1)
            right+=1
        return maxl
