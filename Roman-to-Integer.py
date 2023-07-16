class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == 'I':
                count += 1
            elif s[i] == 'V':
                if i>0:
                    if s[i-1] == 'I':
                        count += 3
                    else:
                        count+=5
                else:
                    count += 5
            elif s[i] == 'X':
                if i>0:
                    if s[i-1] == 'I':
                        count += 8
                    else :
                        count +=10
                else:
                    count += 10
            elif s[i]=='L':
                if i>0:
                    if s[i-1] == 'X':
                        count += 30
                    else:
                        count+=50
                else:
                    count += 50
            elif s[i]=='C':
                if i>0:
                    if s[i-1] == 'X':
                        count += 80
                    else:
                        count+=100
                else:
                    count += 100
            elif s[i]=='D':
                if i>0:
                    if s[i-1] == 'C':
                        count += 300
                    else:
                        count+=500
                else:
                    count += 500
            elif s[i]=='M':
                if i>0:
                    if s[i-1] == 'C':
                        count += 800
                    else:
                        count+=1000
                else:
                    count += 1000


        return count

        
