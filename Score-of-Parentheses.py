class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(len(stack) + 1)
            else:
                x = stack.pop()
                if s[i-1] == '(':
                    count+=2**(x-1)
        return count
 
