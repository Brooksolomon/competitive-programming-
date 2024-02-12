class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mini = float('inf')
        for x,y in ghosts:
            a = abs (x - target[0]) + abs(y-target[1])
            mini = min(a,mini)
        return mini > abs(target[0]) + abs(target[1])
