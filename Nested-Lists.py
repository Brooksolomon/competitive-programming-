if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name,score])
    result.sort(key = lambda x : (x[1],x[0]))
    found = False
    
    ans = []
    for i in result:
        if not found:
            if i[1]!=result[0][1]:
                key = i[1]
                ans.append(i[0])
                found = True
        else:
            if i[1] == key:
                ans.append(i[0])
            else:
                break
    for i in ans:
        print(i)
