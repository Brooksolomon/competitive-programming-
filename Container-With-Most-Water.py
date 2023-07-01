class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left=0
        right = len(height) -1
        for i in range(right) : 
            if min(height[left],height[right]) * (right - left) > maxi:
                maxi=min(height[left],height[right]) * (right - left)
            if height[left] >= height[right]:
                right-=1
            else:
                left+=1
        return maxi
