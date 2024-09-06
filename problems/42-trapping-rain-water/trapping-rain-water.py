class Solution(object):
    def trap(self, height):
        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left<right:
            if leftmax<rightmax:
                left=left+1
                if leftmax<height[left]:
                    leftmax=height[left]
                else:
                    water=leftmax+water-height[left]
            else:
                right=right-1
                if rightmax<height[right]:
                    rightmax=height[right]
                else:
                    water=water+rightmax-height[right]
        return water























        
        