
from collections import Counter
def isSubset( a1, a2, n, m):
    a2 = Counter(a2)
    a1 =Counter(a1)
    for i in a2:
        if a1.get(i,0)>=a2.get(i,0):
            continue
        else:
            return "No"
    return "Yes"
            
    
    
