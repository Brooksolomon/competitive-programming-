class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for p in paths:
            dir = p.split()[0]
            files = list(map(str,p.split()[1:]))
            for f in files:
                file ,content = f.split("(")
                content = content[:-1]
                d[content].append(dir+"/"+file)
        return [d[x] for x in d if len(d[x]) > 1]
                
