class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies) - extraCandies
        for i in range(len(candies)):
            candies [i] = candies[i] >= m
        return candies
        
