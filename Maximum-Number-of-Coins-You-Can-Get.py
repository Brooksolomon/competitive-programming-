class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        total = 0
        for i in range(1,len(piles)-(len(piles))//3,2):
            total+=piles[i]
        return total
        
