class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0 
        r = 0
        maxi = 0
        while r < len(s): 

            window[s[r]] +=1 
            r+=1

            if (r-l) - max(window.values()) <= k: 
                maxi = max(maxi,(r-l))
            
            while (r-l) - max(window.values())  > k:
                window[s[l]]-=1
                l+=1
            
                
        

        return maxi
