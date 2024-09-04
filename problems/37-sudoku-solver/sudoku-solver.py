class Solution(object):
    def solveSudoku(self, board):
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    num=board[i][j]
                    row[i].add(num)
                    col[j].add(num)
                    boxid=i//3*3+j//3
                    box[boxid].add(num)
        def b(i,j):
            if i==9:
                return True
            if j==9:
                return b(i+1,0)
            if board[i][j]!='.':
                return b(i,j+1)
            boxid=i//3*3+j//3
            for nums in map(str,range(1,10)):
                if nums not in row[i] and nums not in col[j] and nums not in box[boxid]:
                    board[i][j]=nums
                    row[i].add(nums)
                    col[j].add(nums)
                    box[boxid].add(nums)
                    if b(i,j+1):
                        return True
                    board[i][j]='.'
                    row[i].remove(nums)
                    col[j].remove(nums)
                    box[boxid].remove(nums)
            return False
        b(0,0)
        


        
        