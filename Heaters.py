class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxi = 0
        heaters.sort()
        for i in houses:
            left = 0
            right = len(heaters) -1
            md = float('inf')
            while left <=right:
                m = left + (right - left) // 2
                md= min(md,abs(heaters[m] - i))
                if heaters[m] < i:
                    left = m + 1
                elif heaters[m] > i:
                    right = m-1
                else:
                    break
            maxi = max (maxi, md)
        return maxi
