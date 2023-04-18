class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x= len(arr)
        n = int(len(arr)/2)
        z=0
        for i,j in sorted(Counter(arr).items(),key=lambda k: -k[1]):
            x-=j
            z +=1
            if x<=(n):
                break
        return z
