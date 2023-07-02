x = list(map(int,input().split()))
n=x[0]
m=x[1]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x= 0
y = 0
arr=[]
for i in range(m+n):
    if x>n-1:
        arr.append(n)
        continue
    elif y > m-1:
        break
    if a[x] < b[y]:
        x+=1
    else:
        arr.append(x)
        y+=1
for i in arr:
    print(i)
