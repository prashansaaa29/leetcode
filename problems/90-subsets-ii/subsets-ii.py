class Solution(object):
    def subsetsWithDup(self, nums):
        p=[]
        def subset(i,nums,s):
            if i==len(nums):
                    p.append(s)
                    return
            subset(i+1,nums,s+[nums[i]])
            subset(i+1,nums,s)
        subset(0,nums,[])
        d=[]
        for i in p:
            i.sort()
            if i not in d:
                d.append(i)
        return d

        