class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                if stack and stack[-1] > 0 :
                    check =False
                    while stack: 
                        if stack[-1] < 0:
                            break   
                        if abs(i) > abs(stack[-1]) and stack[-1] > 0:
                            stack.pop()
                            check=True
                        elif abs(i) == stack[-1]:
                            stack.pop()
                            check=False
                            break
                        else:
                            check= False
                            break
                    if check:
                        stack.append(i)
                else:
                    stack.append(i)

                
        return stack
