x = list(map(int,input().split()))
n=x[0]
m=x[1]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x= 0
y = 0
arr=[]
for i in range(m+n):
    if a[x] > b[y]:
        arr.append(b[y])
        y+=1
    else:
        arr.append(a[x])
        x+=1
    if x>n-1:
        arr+=b[y:]
        break
    elif y > m-1:
        arr+=a[x:]
        break
for i in arr:
    print(i)
