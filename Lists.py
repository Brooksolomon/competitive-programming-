if __name__ == '__main__':
    N = int(input())
    arr = []
    md = {'insert': arr.insert, 'print': print, 'sort': arr.sort, 'pop': arr.pop, 'reverse': arr.reverse,
        'remove': arr.remove, 'append': arr.append}
    for _ in range(N):
        exp = list(map(str, input().split()))
        if exp[0] == 'insert':
            md[exp[0]](int(exp[1]), int(exp[2]))
        elif exp[0] =='print':
            md[exp[0]](arr)
        elif exp[0] in [ 'sort', 'pop', 'reverse']:
            md[exp[0]]()
        else:
            md[exp[0]](int(exp[1]))


            
