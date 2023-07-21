class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c=0
        l = [0] *60
        for i in time:
            x = (60-(i%60)) %60
            c += l[x]
            l[i%60] +=1
        return c
