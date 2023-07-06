class Solution:
    def compress(self, chars: List[str]) -> int:
        left= right = 0
        count=0
        bud=0
        put=0
        while right < len(chars):
            if chars[left] == chars[right]:
                if count==1:
                    chars[put] = chars[left]
                    put+=1
                count+=1
                right+=1
            else:
                if count==1:
                    chars[put] = chars[left]
                    put+=1
                elif count>1:
                    for i in str(count):
                        chars[put] = i
                        left+=1
                        put+=1
                    bud = left+1
                count = 0
                left=right
        if count == 1:
            chars[put] = chars[left]
            put += 1
        elif count > 1:
            for i in str(count):
                chars[put] = i
                left += 1
                put+=1
            bud = left+1

        print(chars)
        return put


                    
