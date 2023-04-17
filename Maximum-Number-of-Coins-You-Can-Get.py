class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        lst = piles[1:len(piles) - int(len(piles) /3) :2]
        return sum(lst)
