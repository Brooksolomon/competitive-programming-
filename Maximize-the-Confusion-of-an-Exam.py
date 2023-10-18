class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if len(answerKey) == 1 and k == 1:
            return 1
        if 'T' not in answerKey or 'F' not in answerKey:
            return len(answerKey)
        maxi = 0
        count = 0
        l = 0
        window = {}
        for r in range(len(answerKey)):
            window[answerKey[r]] = window.get(answerKey[r],0) + 1
            if (len(window.keys()) == 2):
                if (window['T'] <= k or window['F'] <= k):
                    maxi = max(max_len, r - l + 1)
                if (window['T'] > k and window['F'] > k):
                    window[answerKey[l]] -= 1
                    l += 1
            else:
                max_len = max( maxi, r - l + 1)

 
        return maxi 


            


            
            


            
