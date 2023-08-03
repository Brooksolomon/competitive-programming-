class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
            l , r = 0 ,1
            result = 1
            sign = "="
            while r<len(arr):
                if arr[r-1] > arr[r] and sign != ">":
                    r+=1
                    sign = ">"
                elif arr[r-1] < arr[r] and sign !="<":
                    r+=1
                    sign = "<"
                else:
                    print(r,l)
                    result = max(result,(r - l))
                    if arr[r] == arr[r-1]:r+=1
                    l = r-1
                    sign="="
             
            return  max(result,(r - l))
            
