class Solution(object):
    def solveNQueens(self, n):
        col=set()
        posid=set()
        negad=set()
        res=[]
        board=[["."]*n for i in range(n)]
        def b(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r-c) in negad or (r+c) in posid:
                    continue
                col.add(c)
                posid.add(r+c)
                negad.add(r-c)
                board[r][c]='Q'
                b(r+1)
                col.remove(c)
                posid.remove(r+c)
                negad.remove(r-c)
                board[r][c]='.'
        b(0)
        return res


        