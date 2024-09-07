class Solution(object):
    def isValidSudoku(self, board):

        row= defaultdict(set)
        cols= defaultdict(set)
        sqaure= defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if (board[i][j] in row[i] or board [i][j] in cols[j] or board[i][j] in sqaure[(i//3,j//3)]):
                    return False
                    

                else:
                    row[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sqaure[(i//3,j//3)].add(board[i][j])
        return True


                


        
                    

         
        