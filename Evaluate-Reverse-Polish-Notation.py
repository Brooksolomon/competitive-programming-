class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        operators = {"+", "-", "*","/"}
        for i in tokens:
            if i in operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.math(int(x),int(y),i))
            else:
                stack.append(i)
        return int(stack.pop())
    def math(self,x,y,op):
        if op=='+':
            return x+y
        elif op=='-':
            return x-y
        elif op=='*':
            return x*y
        return math.trunc(x/y)
