class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3:
            return []
        else:
            x = num//3
            return [x-1,x,x+1]
