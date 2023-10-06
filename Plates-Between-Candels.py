class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        idx = []
        ans = []
        for i,e in enumerate(s):
            if e=='|':
                idx.append(i)
        for x,y in queries:
            l = bisect_left(idx,x)
            r = bisect_right(idx,y) - 1
            if r<l:
                ans.append(0)
                continue
            temp = r - l - 1
            q = idx[r] - idx[l] -1
            ans.append(q-temp)
        return ans
        
