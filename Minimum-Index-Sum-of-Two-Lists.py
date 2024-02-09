class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        first = {}
        second = {}
        for i,e in enumerate(list1):
            first[e]=i
        for i,e in enumerate(list2):
            second[e] = i
        ans = []
        count = float('inf')
        for i in first:
            if i in second:
                if first[i] + second[i] < count:
                    ans = [i]
                    count = first[i] + second[i]
                elif first[i] +second[i] == count:
                    ans.append(i)
                    count = first[i] + second[i]
        return ans

