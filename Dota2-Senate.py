class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q=list(senate) 
        left=1    
        while len(set(q)) >1:
            if q[0] != q[left]:
                q.append(q[0])
                q.pop(left)
                q.pop(0)
                left-=2
            left+=1
        if q[0] == 'R':
            return "Radiant"
        else:
            return"Dire"

                
               

                
