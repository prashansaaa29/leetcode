class Solution(object):
    def findDuplicate(self, nums):
        p=sum(nums)
        #o=max(nums)
        o=sum(set(nums))#(o*(o+1))//2
        b=len(nums)-len(set(nums))
        return (p-o)/b


        