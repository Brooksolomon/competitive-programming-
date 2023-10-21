class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        md ={']':'['
            ,'}':'{',
            ')':'('}
        openers = set({'(','{','['})
        for i in s:
            if i in openers:
                stack.append(i)
            elif stack:
                if stack[-1] == md[i]:
                    stack.pop()
                else:
                    return False 
            else:
                return False
        if stack:
            return False 
        return True
