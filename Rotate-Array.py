class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)==0 or len(nums)==1:
            return
        left = 0
        k = k%(len(nums))
        right = len(nums) - k
        replaced =deque()
        pointer = 0
        while right < len(nums):
            replaced.append(nums[left])
            nums[left] = nums[right]
            left+=1
            right+=1
        while left < len(nums) - k:
            replaced.append(nums[left])
            nums[left] = replaced[pointer]
            pointer+=1
            left+=1
        while pointer  < len(replaced) and left < len(nums):
            nums[left] = replaced[pointer]
            pointer+=1
            left+=1
