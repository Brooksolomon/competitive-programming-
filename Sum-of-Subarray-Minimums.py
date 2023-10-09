class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 1e9 + 7
        st = []
        dp = [0] * n
        sum = 0
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if not st:
                dp[i] = (i + 1) * arr[i]
            else:
                dp[i] = dp[st[-1]] + (i - st[-1]) * arr[i]
            sum = (sum + dp[i]) % mod
            st.append(i)
        return int(sum)
