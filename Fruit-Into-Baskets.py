class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <=2 or len(set(fruits)) <=2 :
            return len(fruits)
        maxi = cur = left = 0
        mydict = defaultdict(int)
        for i in range(len(fruits)):
            mydict[fruits[i]] += 1
            cur += 1
            while len(mydict) > 2:
                key = fruits[left]
                mydict[key] -= 1
                cur -= 1
                left += 1
                if not mydict[key]:
                    mydict.pop(key)
                    break
            maxi = max(maxi, cur)
        return maxi
