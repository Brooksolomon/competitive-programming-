class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        count=Counter(s)

        x = sorted(count.items(),key=lambda x:x[1],reverse=True)

        ans=""
        for i in x:
            ans+=(i[0])*i[1]

        return (ans)
