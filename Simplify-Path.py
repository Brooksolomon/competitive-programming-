class Solution:
    def simplifyPath(self, s: str) -> str: 
        stack = []
        s = s.split('/')
        for i in s:
            if i  == '' or i == '.':
                continue
            elif i=='..':
                if stack :
                    stack.pop()
            else:
                stack.append('/'+i)
        if not stack:
            return '/'
        return "".join(stack)


        
