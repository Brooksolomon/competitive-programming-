class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            ans = []
            right = len(p)
            s= list(s)
            m =  s[0:right]
            left = 0
            pd = list(dict(Counter(p)).items())
            for i in range(len(s) -  (right)):
                md = list(dict(Counter(m)).items())
                if all(x in md for x in pd):
                    ans.append(left)
                right+=1
                left+=1
                m.pop(0)
                m.append(s[right-1])
            md = list(dict(Counter(m)).items())
            if all(x in md for x in pd):
                ans.append(left)
            return ans
                

