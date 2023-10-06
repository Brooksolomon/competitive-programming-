class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        keyer = sorted(arr)
        p = len(arr) -1
        ans = []
        for i in range(p+1):
            x = arr.index(keyer[p])
            arr = list(reversed(arr[:x+1])) + arr[x+1:]
            arr = list(reversed(arr[:p+1]) )+ arr[p+1:]
            ans.append(x+1)
            ans.append(p+1)
            p-=1
        return ans
        


