class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        for i in range(len(ages)):
            ans += max(0,(bisect.bisect_right(ages, ages[i])-1)-bisect.bisect_left(ages,int(ages[i]*0.5+8)))
        return ans
