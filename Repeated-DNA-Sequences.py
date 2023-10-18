class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l=-1
        r = 8
        md = {}
        ans = set()

        while r< len(s):
            r+=1
            l+=1
            if md.get(s[l:r+1],None):
                ans.add(s[l:r+1])
            else:
                md[s[l:r+1]] =  1
        return ans


