class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0 
        l=0
        r=0
        x = len(s)
        while r < x:
            if s[l] == s[r]:
                r+=1
            else:
                count += ((r - l+1) * (r - l)) //2 
                l=r
        count += (((r - l)+1) * (r - l)) //2 
        return count % (10**9 + 7)

        
        
