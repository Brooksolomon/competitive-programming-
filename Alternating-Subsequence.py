t = int(input())

for j in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check = False
    arr=[]
    arr.append(a[0])
    if a[0] > 0:
        check = False
    else:
        check = True
    for i in range(1,n):
        if (a[i] > 0) == check:
            arr.append(a[i])
            check=not check
        else:
            if (a[i] > 0):
                if a[i] > arr[-1]:
                    arr.pop()
                    arr.append(a[i])
            else:
                if a[i] > arr[-1]:
                    arr.pop()
                    arr.append(a[i])

    print(sum(arr))
