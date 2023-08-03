class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        m = bisect.bisect_left(arr,x)
        if m-1 >= 0 and m<len(arr) and abs(arr[m-1] - x) <= abs(arr[m]-x):
            m-=1
        left = right = m
        if m<len(arr):
            k -= 1
        while k > 0:
            if left > 0 and right < len(arr) - 1:
                if abs(x - arr[left-1]) <= abs(x - arr[right+1]):
                    left -= 1
                    k -= 1
                else:
                    right += 1
                    k -= 1
            elif left > 0:
                left -= 1
                k -= 1
            elif right < len(arr) - 1:
                right += 1
                k -= 1

        return arr[left:right+1]
        
