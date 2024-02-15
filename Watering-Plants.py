class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        jug = capacity
        for i,e in enumerate(plants):
            if jug >= e:
                steps+=1
                jug-=e
            else:
                steps+=(i)*2 + 1
                jug = capacity - e
        return steps


        
