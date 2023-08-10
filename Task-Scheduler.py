class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mydict = Counter(tasks)
        time = 0                  
        n += 1                      
        while mydict:
            current = mydict.most_common(n)
            len_cur = len(current)
            time += len_cur
            for k, _ in current:
                if mydict[k] > 1:
                    mydict[k] -= 1
                else:
                    del mydict[k]    
            if mydict:
                time += n - len_cur
        return time
