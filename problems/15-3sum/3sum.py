class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        target=0
        s=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    s.add((nums[i],nums[j],nums[k]))
                    j=j+1
                    k=k-1
                elif sum>target:
                    k=k-1
                elif sum<target:
                    j=j+1
        o=list(s)
        return o
                



        