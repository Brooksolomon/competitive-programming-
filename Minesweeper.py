class Solution:
    def valid(self,x,y,board):
        if x < 0 or y < 0 or x == len(board) or y==len(board[0]):
            return False
        return True

    def adjacent(self,board,x,y):
        self.direction = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        count = 0
        for a,b in self.direction:
            if self.valid(x+a,y+b,board) and board[x+a][y+b] == 'M':
                count+=1
        return count
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        x,y  = click
        if board[x][y] =='M':
            board[x][y] = 'X'
        else:
            if self.adjacent(board,x,y):
                board[x][y] = str(self.adjacent(board,x,y))
            else:
                board[x][y] = 'B'
                for a,b in self.direction:
                    if self.valid(x+a,y+b,board) and board[x+a][y+b]!='B':
                        self.updateBoard(board,[x+a,y+b])
        return board

        


        
        
