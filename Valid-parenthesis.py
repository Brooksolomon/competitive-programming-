class Solution:
    def isValid(self, s: str) -> bool:
        opener = list()
        count = -1

        check = True
        for elem in s:
            if elem =="(" or elem=="[" or elem=="{":
                opener.append(elem)
                count +=1
            else:
                if count > -1:
                    if elem==")":
                        if opener[count] == "(":
                            opener.pop(count)
                            count-=1
                        else:
                            check = False
                            break

                    elif elem=="]":
                        if opener[count] == "[":
                            opener.pop(count)
                            count -= 1
                        else:
                            check = False
                            break
                    elif elem=="}":
                        if opener[count] == "{":
                            opener.pop(count)
                            count -= 1
                        else:
                            check = False
                            break
                else:
                    check = False
        if len(opener) !=0:
            check = False

        
        return check
