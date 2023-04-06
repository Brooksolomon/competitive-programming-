n,m,a = map(int,input().split())

if n > a or m > a:
    if n % a != 0:
        n_count = int(n / a) + 1
    else:
        n_count = (n / a) 
    if m % a != 0:
         m_count = int(m / a) + 1
    else:
        m_count = (m / a) 
    print(int(n_count*m_count))
else:
    print(1)
    


    
    
