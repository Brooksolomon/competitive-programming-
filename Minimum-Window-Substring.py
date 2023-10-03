class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        md = Counter(t)
        tempd = defaultdict(int)
        r = 0
        l = 0
        mini = float('inf')
        for i in s:
            tempd[i] += 1
            check = True
            r += 1
            for j in md.keys():
                if tempd[j] < md[j]:
                    check = False
                    break
            else:
                check = False
                for i in range(l,len(s)):
                    tempd[s[i]] -= 1
                    for j in md.keys():
                        if tempd[j] < md[j]:
                            check = True
                            if r - l < mini:
                                mini = r - l
                                ans = s[l:r]
                                
                                break
                    l += 1
                    if check:
                        break
        return ans
