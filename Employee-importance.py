"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mydict = dict()
        for x in employees:
            mydict[x.id] = x
        ans=[0]
        def dfs(node):
            ans[0] += node.importance
            if not node.subordinates:
                return 
            
            for x in node.subordinates:
                dfs(mydict[x])


        for i in employees:
            if i.id==id:
                dfs(i)
                break
        return ans[0]
