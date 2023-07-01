class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=[]
        for i in s:
            if i.isalnum():
                x.append(i)
        s="".join(x)
        s=s.lower()

        n=len(s)
        for i in range(n):
            if s[i]==s[n - 1 - i]:
                continue
            else:
                return False

        return True
