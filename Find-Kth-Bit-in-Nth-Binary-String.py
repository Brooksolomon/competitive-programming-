class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans=[]
        def find(s,z):
            if z==n+1:
                return s
            x=''
            for i in s:
                if i =='1':
                    x+='0'
                else:
                    x+='1'

            return find((s + "1" +str(x[::-1])), z+1)
        r =  find("0",1)
        return r[k-1]
