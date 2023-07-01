class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        left = 0 
        right=len(people) - 1
        for i in range(len(people)):
            if people[left] + people[right] <= limit:
                boats += 1
                left+=1
                right-=1
            else:
                boats += 1 
                right-=1 
            if left ==right:
                return boats+1
            elif left > right:
                break         
        return boats
