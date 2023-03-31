    M=0
    N=0

    def Dominos(x):
        dominos=0
        for i in range(0,x):
            if  x-1>0:
                x-=2
                dominos+=1  
        return dominos




    M,N=map(int,input().split())


    x=M*N

    print(Dominos(x))


