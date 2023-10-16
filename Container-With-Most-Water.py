class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) -1 
        maxi = 0
        while left < right :
            maxi = max(min(height[right],height[left]) * (right - left),maxi)

            if height[right] >= height[left]:
                left+=1
            else:
                right-=1
        return maxi

        
