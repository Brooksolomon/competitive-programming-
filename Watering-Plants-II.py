class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left=0
        right = len(plants) -1 
        a = capacityA
        b = capacityB
        count = 0
        while left<right:
            if a >= plants[left]:
                a -= plants[left]
                left+=1
            else:
                a = capacityA - plants[left]
                left+=1
                count+=1
            
            if b >= plants[right]:
                b -= plants[right]
                right-=1
            else:
                b = capacityB - plants[right]
                right-=1
                count+=1
        return count +  (int(max(a,b) < plants[left]) if left==right else 0)
            



        
