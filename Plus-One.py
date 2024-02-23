class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        n = len(digits) -1
        for i in range(n,-1,-1):
            if digits[i]  + rem  + (n == i)>9 :
                digits[i] = 0
                rem = 1
            else:
                digits[i] = digits[i]  + rem + (n==i)
                rem = 0
                break
        if rem:
            return [1] + digits
        return digits
