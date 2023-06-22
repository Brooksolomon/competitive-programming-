class Solution:
    def reverseString(self, s: List[str]) -> None:
        def recc ( x , y , s):
            if x>=y:
                return
            s[x],s[y] = s[y],s[x]
            recc(x+1,y-1,s)
        y=len(s) - 1
        recc(0,y,s)
        
        
