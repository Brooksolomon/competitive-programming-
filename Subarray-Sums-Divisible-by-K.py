class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict = defaultdict(int)
        mydict[0]=1
        sum = 0
        count = 0
        for i in nums:
            sum+=i
            reminder = sum % k
            count += mydict[reminder]
            mydict[reminder]+=1
        return count

            
