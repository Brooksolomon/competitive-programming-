class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        ans = ""
        n = min(len(word1),len(word2))
        while l < n and l < n:
            ans+=word1[l]
            ans+=word2[l]
            l+=1
        if l < len(word1) :
            ans+=word1[l:]
        if l < len(word2) :
            ans+=word2[l:]
        return ans
