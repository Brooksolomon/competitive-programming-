class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutaions = []

        def helper(nums, cur,already_done,permutaitons):
            if len(cur) == len(nums):
                permutaions.append(cur[:])
                return
            
            for num in nums:
                if num not in already_done:
                    already_done.add(num)
                    cur.append(num)
                    helper(nums,cur,already_done,permutations)
                    already_done.remove(num)
                    cur.pop()
        
        helper(nums,[],set(),permutations)
        return permutaions
