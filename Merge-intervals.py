class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a : a [0])

        answer=[intervals[0]]

        for inter in intervals[1:]:
            if  inter[0]  <= answer[-1][1]:
                answer[-1][1]=max(inter[1],answer[-1][1])
            else :
                answer.append([inter[0],inter[1]])




        return answer
