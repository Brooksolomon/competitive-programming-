class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum = []
        ans = float('inf')
        presum.append(nums[0])
        for i in nums:
            presum.append(i+presum[-1])
        q = deque()
        for i in range(len(presum)):
            while q and presum[i] <=presum[q[-1]]:
                q.pop()
            while q and presum[i] - presum[q[0]] >=k:
                ans = min(ans,i-q.popleft())
            q.append(i)
        
        return -1 if ans==float('inf') else ans
        
