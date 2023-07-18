class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans =[]
        def helper(ss,id):
            if id==len(graph)-1:
                ans.append(ss[:])
                return 


            for i in graph[id]:
                ss.append(i)
                helper(ss,i)
                ss.pop()
        helper([0],0)
        return ans
        
