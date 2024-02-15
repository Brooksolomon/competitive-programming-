class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        md = defaultdict(int)
        for i in cpdomains:
            num,url = map(str,i.split())
            num = int(num)
            a  = list(map(str,url.split('.')))
            if len(a) ==3:
                md[url] += num
                md[a[1]+'.'+a[2]] +=num
                md[a[2]] +=num
            else:
                md[url]+=num
                md[a[1]]+=num
        ans = []
        for i in md:
            ans.append(str(md[i])+' '+i)
        return ans
