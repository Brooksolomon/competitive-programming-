class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        x=[]
        ans=[]
        for i in mat:
            x.append(i.count(1))
        print(x)
        dc = defaultdict(list)
        for i,e in enumerate(x):
            dc[e].append(i)
        heapify(x)
        for i in range(k):
            j = heappop(x)
            ans.append(dc[j].pop(0))
        return ans

