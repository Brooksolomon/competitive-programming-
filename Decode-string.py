class Solution:
    def decodeString(self, s: str) -> str:

            
        def decode(c,ns,ss,ans):
            if c == len(s):
                print(ss)
                return ss
            if s[c].isnumeric():
                ns=ns*10 + int(s[c])
            elif s[c]=='[':
                ans.append(ss)
                ans.append(ns)
                ss=""
                ns=0
            elif s[c]==']':
                current = ans.pop()
                prev= ans.pop()
                ss = prev + current * ss
            else:
                ss+=s[c]
            return decode(c+1,ns,ss,ans)
    
        return decode(0,0,"",[])
