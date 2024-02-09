n = int(input())
total = 0
maxi = 0
for _ in range(n):
    a,b = map(int,input().split())
    total+=b
    total-=a
    maxi = max(maxi,total)
print(maxi)
    
