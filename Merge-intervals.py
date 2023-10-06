class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda a:a[0])
        p=0
        n = len(intervals)
        while p < n-1:
            if intervals[p][1] >= intervals[p+1][0]:
                intervals[p][1] = max(intervals[p+1][1],intervals[p][1])
                intervals.pop(p+1)
                n-=1
            else:
                p+=1
        return intervals
