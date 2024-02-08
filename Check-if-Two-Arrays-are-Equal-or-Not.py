from collections import Counter
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        return sorted(Counter(A).items()) == sorted(Counter(B).items())
