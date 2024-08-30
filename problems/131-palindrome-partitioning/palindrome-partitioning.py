class Solution(object):
    def partition(self, s):
        res=[]
        def b(i,curr):
            if i==len(s):
                res.append(curr[:])
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    b(j+1,curr)
                    curr.pop()
        b(0,[])
        return res









            
        