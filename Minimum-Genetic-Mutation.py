class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:return -1
        if startGene == endGene:return 0
        
        visited = set()
        queue = deque()
        queue.append((startGene,0))
        while queue:
            n =  len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur[0] in visited:
                    continue
                visited.add(cur[0])
                for j in bank:
                    if cur[0] == endGene:
                        return cur[1]
                    elif self.compare(cur[0],j)  :
                        queue.append((j,cur[1]+1))
        return -1




    def compare(self,x,y):
        check = True
        for i in range(8):
            if x[i] == y[i]:
                continue
            elif check:
                check = False
                continue
            else:
                return False
        return True
