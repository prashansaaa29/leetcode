class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        k=g
        c=0
        i=0
        j=0
        while i<len(s) and j<len(g):
                if s[i]>=g[j]:
                    c+=1
                    i=i+1
                    j=j+1
                elif g[j]>s[i]:
                    i=i+1
        return c





        