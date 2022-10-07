class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print(board)
        
        n  = len(board)
        boxes = [set() for _ in range(n)]
        #print(n)
        for i in range(n):
            
            rows = set()
            cols = set()
            
            for j in range(n):
                
                if board[i][j]=='.': continue
                    
                if board[i][j] in rows:
                    return False
                
                rows.add(board[i][j])
                
                boxNumber = 3*(i//3) + j//3
                
                if (board[i][j] in boxes[boxNumber]):
                    return False
                
                boxes[boxNumber].add(board[i][j])
                
            for j in range(n):
                
                if board[j][i]=='.': continue
                    
                if board[j][i] in cols:
                    return False
                
                cols.add(board[j][i])
                
        return True
                
                