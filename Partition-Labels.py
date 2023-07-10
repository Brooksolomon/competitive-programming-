class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        Final = []
        one = two = 0 
        for i in range(len(s)):
            two = max(two,s.rindex(s[i]))
            if i == two:
                Final.append(two-one+1)
                one = two + 1
        return Final
                  
        


            
