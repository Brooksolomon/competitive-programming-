class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = []
        for i in range(len(position)):
            x.append((position[i],speed[i]))
        x.sort(key=lambda i:i[0])
        new=[]
        for i in range(len(position)):
            new.append((target - x[i][0]) / x[i][1])
        stack = [new[-1]]
        for i in range(len(new)-2,-1,-1):
            if stack[-1] >= new[i]:
                continue
            else:
                stack.append(new[i])
        return(len(stack))
