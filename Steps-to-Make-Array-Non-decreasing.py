class Solution:
    def totalSteps(self, nums):

        max_eat = [0] * len(nums)
        stack = []
        steps = 0

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                max_eat[i] = max(max_eat[i] + 1, max_eat[stack[-1]])
                stack.pop()

            stack.append(i)
            steps = max(steps, max_eat[i])

        return steps

