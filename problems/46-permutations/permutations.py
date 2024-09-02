class Solution(object):
    def permute(self, nums):
        res=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(i)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.insert(i,n)
        return res
        
        