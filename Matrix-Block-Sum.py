class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        l = len(mat)
        w = len(mat[0])
        prefixSum = [[0] * w for i in range(l)]
        for r in range(l):
            x = 0
            for c in range(w):
                x+=mat[r][c]
                prefixSum[r][c] = x
        sub = [[0] * w for i in range(l)]
        for r in range(l):
            for c in range(w):
                x = (max(0,r-k) , min(r+k,l-1))
                y = (max(0,c-k) , min(c+k,w-1))
                temp = 0
                for q in range(x[0],x[1] + 1):
                    a = prefixSum[q][y[1]]
                    b = prefixSum[q][y[0]]
                    d = mat[q][y[0]]
                    temp += a+d - b
                sub[r][c] = temp
        return sub
            


