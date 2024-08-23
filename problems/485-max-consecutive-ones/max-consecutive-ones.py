class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        t=0
        for i in nums:
            if i==1:
                c=c+1
                t=max(t,c)
            else:
                c=0
        return t

        