class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones)>1:
            x=heappop(stones)
            y=heappop(stones)
            if x-y !=0:
                heappush(stones,x-y)


        if stones:return -stones[0]
        else:return 0
