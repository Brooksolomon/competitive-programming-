for _ in range(int(input())):
    n,a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    l = 0
    r = n -1
    res = 0
    while l < r:
        if arr[l] + arr[r] > b:
            r-=1
        else:
            res+=r - l
            l+=1
    l = 0
    r = n - 1
    while l < r:
        if arr[l] + arr[r] > a-1:
            r -= 1
        else:
            res -= r - l
            l += 1
    print(res)
