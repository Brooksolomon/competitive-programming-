class Solution:
    def largestInteger(self, num: int) -> int:
        ans=[]
        num = list(str(num))
        clone = num.copy()
        nume = [-int(i) for i in num if int(i)%2==0]
        numo = [-int(i) for i in num if int(i)%2!=0]
        heapify(num)
        heapify(nume)
        heapify(numo)
        for i in clone:
            if int(i)%2==0:
                ans.append(str(-heappop(nume)))
            else:
                ans.append(str(-heappop(numo)))
        return int("".join(ans))
