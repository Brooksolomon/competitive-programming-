class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            right = len(s1)
            s = list(s2)
            s2=list(s2)
            m = s2[0:right]
            left = 0
            pd = list(dict(Counter(s1)).items())
            for i in range(len(s2) - (right)):
                md = list(dict(Counter(m)).items())
                if all(x in md for x in pd):
                    return True
                right += 1
                left += 1
                m.pop(0)
                m.append(s[right - 1])
            md = list(dict(Counter(m)).items())
            if all(x in md for x in pd):
                return True
            return False
