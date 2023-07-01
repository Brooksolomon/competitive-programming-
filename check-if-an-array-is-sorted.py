class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True
