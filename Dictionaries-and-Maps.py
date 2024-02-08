# Enter your code here. Read input from STDIN. Print output to STDOUT
md = {}
for _ in range(int(input())):
    name, phone = map(str, input().split())
    md[name] = phone
x = input()
while(x):
    if x in md:
        print(f'{x}={md[x]}')
    else:
        print("Not found")
    try:
        x = input()
    except:
        break
     
    
    
