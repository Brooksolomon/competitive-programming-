class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words) 
        m = len(words[0])
        l = -1
        r = n * m - 2
        c = Counter(words)
        ans = []
        while r < len(s):
            l += 1
            r += 1
            x = l
            y = x + m-1
            temp = c.copy()
            while y <=r:
                if temp.get(s[x:y+1], None):
                    if temp.get(s[x:y+1]) == 1:
                        temp.pop(s[x:y+1])
                    else:
                        temp[s[x:y+1]] -=1
                    
                    x += m
                    y = x + m-1
                else:
                    break
            else:
                ans.append(l)
        return ans



