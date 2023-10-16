class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)<2:
            return 
        left = 0
        right = 1
        write = 0
        while right <= len(chars) :
            if right < len(chars) and  chars[left] == chars[right]:
                while right < len(chars)  and chars[left] == chars[right]:
                    right+=1
                val = str((right-left))
                chars[write]=chars[left]
                write+=1
                for i in val:
                    chars[write] = i
                    write+=1
                    

                left=right
                right+=1
            else:
                chars[write] = chars[left]
                left+=1
                right+=1
                write+=1


        for _ in range(len(chars) - write):
            chars.pop()
            
        
