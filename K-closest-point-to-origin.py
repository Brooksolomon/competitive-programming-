import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        ans = []
        for x, y in points:
            arr += [[x**2 + y**2, x, y]]

        heapq.heapify(arr)

       
        for i in range(k):
            d, x, y = heapq.heappop(arr)
            ans.append([x, y])

        return ans
