#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=[0]*n
        leftmax[0]=height[0]
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i])

        rightmax=[0]*n
        rightmax[-1]=height[-1]
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])

        ans=0
        for i in range(1,n-1):
            ans+=min(leftmax[i],rightmax[i])-height[i]

        return ans

# @lc code=end

