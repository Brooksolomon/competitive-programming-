class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mydict = {}
        for i in "qwertyuiopQWERTYUIOP":
            mydict[i] = 1
        for i in "asdfghjklASDFGHJKL":
            mydict[i] = 2
        for i in "zxcvbnmZXCVBNM":
            mydict[i] = 3

        ans = []
        for i in words:
            start = mydict[i[0]]
            for j in i:
                if mydict[j] !=start:
                    break
            else:
                ans.append(i)
        return ans


