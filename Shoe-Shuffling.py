t =  int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    l=0
    r=1
    valid = True
    result = []
    while r<=n:
        temp = [l+1]
        while r < n and a[l] == a[r]:
            temp.append(r+1)
            r+=1
        x = len(temp)
        if x==1:
            valid   = False
            break
        result.append((temp.pop()))
        result += temp
        l = r
        r+=1
    if not valid:
        print(-1)
        continue
    print(*result)


