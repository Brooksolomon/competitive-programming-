def swap_case(s):
    ans = ""
    for i in s:
        if i.islower():
            ans+=i.upper()
        else:
            ans+=i.lower()
    return ans
            
    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
