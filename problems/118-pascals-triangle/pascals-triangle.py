class Solution(object):
    def generate(self, numRows):
        a=[[1],[1,1]]
        o=1
        p=1
        b=[1,1]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return a
        for i in range(numRows-2):
            c=[1]
            for k in range(len(b)-1):
                d=b[k]+b[k+1]
                c.append(d)
            c.append(1)
            a.append(c)
            b=c
        return a
        



        
        