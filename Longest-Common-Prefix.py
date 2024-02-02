class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxi = min(strs,key = len)
        if not maxi:
            return ""
        for i in range(len(maxi)):
            check = True
            for j in strs:
                if j[i] !=maxi[i] :
                    check = False
                    break
            if not check:
                break
            i+=1
        return strs[0][:i]
