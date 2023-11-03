class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        myElementsSet= set(target)
        for i in range(1,target[-1]+1):
            operations.append("Push")
            if i not in myElementsSet:
                operations.append("Pop")

        return operations 
            
                
