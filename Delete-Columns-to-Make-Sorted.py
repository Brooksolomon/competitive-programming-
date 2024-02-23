class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        chars = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

        md = defaultdict(int)
        n = len(strs[0])
        count = 0
        for i in strs:
            for j in range(n):
                if md[j] ==-1:
                    continue
                elif md[j] > chars[i[j]]:
                    count+=1
                    md[j] =-1
                else:
                    md[j] = chars[i[j]]
        return count

        
