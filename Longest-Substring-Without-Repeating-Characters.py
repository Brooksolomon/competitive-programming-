class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(set(s)) == len(s):
            return len(s)
        
        ans = ""
        for i in range(len(s)):
            ans+=s[i]
            if len(ans) ==len ( set(ans)):
                continue
            else:
                if len(ans)-1 > maxi:
                    maxi=len(ans)-1
                ans=ans[1:]
        if len(ans) > maxi:
                maxi=len(ans)
        return maxi
                
