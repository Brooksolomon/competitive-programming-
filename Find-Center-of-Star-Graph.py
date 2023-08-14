class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        md = defaultdict(set)
        for i,j in edges:
            md[i].add(j)
            md[j].add(i)
        x = len(md) -1
        for i in md:
            if len(md[i]) == x:
                return i

