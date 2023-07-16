t = int(input())
for j in range(t):
    n , c = input().split()
    s = input()
    if c == 'g':
        print(0)
        continue
    s+=s
    maxi=0
    i = 0
    while i<int(n):
        if s[i] == c:
            l = i
            while s[i] !='g':
                i+=1
            maxi = max(maxi,i-l)
        else:i+=1


    print(maxi)
