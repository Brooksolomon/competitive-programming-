class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sh=[]
        th=[]
        for i in s:
            if i=='#':
                if sh:
                    sh.pop()
            else:sh.append(i)
        for i in t:
            if i=='#':
                if th:
                    th.pop()
            else:th.append(i)
        return sh==th
