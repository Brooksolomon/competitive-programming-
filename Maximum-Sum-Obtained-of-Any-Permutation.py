class Solution:
    def maxSumRangeQuery(self, n: List[int], r: List[List[int]]) -> int:

        p = len(n)
        q = len(r)
        v = [0] * p

        # Calculate prefix sum for range queries
        for i in range(q):
            start = r[i][0]
            end = r[i][1]
            v[start] += 1
            if end + 1 < p:
                v[end + 1] -= 1

        # Calculate cumulative counts
        for i in range(1, p):
            v[i] += v[i - 1]

        # Sort the cumulative counts and the input array in decreasing order
        v.sort(reverse=True)
        n.sort(reverse=True)

        # Calculate the maximum sum
        max_sum = 0
        MOD = 1000000007
        for i in range(p):
            max_sum = (max_sum + n[i] * v[i]) % MOD

        return max_sum
