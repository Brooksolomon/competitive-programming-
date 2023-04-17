class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        new=[]
        while n > 1:
            maxi = max(arr[:n])
            x= arr.index(maxi)
            new.append(x+1)
            new.append(n)
            arr = list(reversed(arr[:x+1]))  + arr[x+1:]
            arr = list(reversed(arr[:n])) + arr [n:]
            n-=1
        return new
