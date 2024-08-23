class Solution(object):
    def removeDuplicates(self, nums):
        v=set()
        i=0
        while i<len(nums):
            if nums[i] not in v:
                v.add(nums[i])
                i=i+1
            else:
                nums.pop(i)
            
    
        
        """
        :type nums: List[int]
        :rtype: int
        """
        