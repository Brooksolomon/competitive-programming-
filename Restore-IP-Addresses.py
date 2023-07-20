class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        if len(s) > 12:
            return []
        def check_validity(a):
            if int(a) > 255 or int(a) < 0:
                return False
            elif (int(a) < 10 and len(a) >1) or (int(a) < 100 and len(a) >2):
                return False    
            return True
        
        ans=[]
        def helper(i,d,c):
            if d==4 and i==len(s):
                ans.append(c[:-1])
                return 
            
            for x in range(i,min(i+3,len(s))):
                if check_validity(s[i:x+1]):
                    helper(x+1,d+1,c+s[i:x+1]+'.')
        helper(0,0,"")
        return ans
                    
             
