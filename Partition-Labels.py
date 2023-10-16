class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        Final = []
        lastappend = maxindex = 0 
        md = {}
        for i in set(s):
            md[i] = s.rindex(i)
        for i in range(len(s)):
            maxindex = max(maxindex,md.get(s[i],0))
            if i == maxindex:
                Final.append(maxindex-lastappend+1)
                lastappend = maxindex + 1
        return Final
