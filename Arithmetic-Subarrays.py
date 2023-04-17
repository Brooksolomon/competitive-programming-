class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        for i in range(len(l)):
            lst = nums[l[i]:r[i]+1]
            lst.sort()
            m=len(lst)
            art = True
            for j in range(m-2):
                if lst[j] - lst[j+1] != lst[j+1] - lst[j+2] :
                    art = False
                    break
            answer.append(art)

        return answer
