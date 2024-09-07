class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        
        s=set(nums)
        l=list(s)
        l.sort()
        print(l)
        if len(l)==1:
            return 1
        c=1
        t=0
        for i in range(len(l)):
            if l[i-1]==l[i]-1:
                c=c+1
                t=max(t,c)
            else:
                c=1
                t=max(c,t)
        return t

        