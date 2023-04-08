class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1
        answer = 0
        nums.sort()

        while start < end and len(nums ) > 0:
            if nums[start] + nums[end] == k:
                answer +=1
                nums.pop(end)
                nums.pop(start)
                end -= 2
            elif nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1

                

        return answer
