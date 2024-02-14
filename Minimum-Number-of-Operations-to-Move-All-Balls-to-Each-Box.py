class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        myset = set()
        for i in range(len(boxes)):
            if boxes[i] == '1' :
                myset.add(i)
        ans = []
        for i in range(len(boxes)):
            count = 0
            for j in myset:
                count+= abs(i-j)
            ans.append(count)
        return ans

        
