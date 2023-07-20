class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mu=float('inf')
        d = [0] *k

        def helper(i):
            nonlocal mu,d
            if i==len(cookies):
                mu = min(mu,max(d))
                return 
            if mu <= max(d):return 
            for x in range(k):
                d[x] += cookies[i]
                helper(i+1)
                d[x] -= cookies[i]
        helper(0)
        return mu
