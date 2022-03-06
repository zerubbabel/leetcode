#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i,j=0,n-1
        ans=(n-1)*min(height[0],height[-1])
        while i<j:
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            ans=max(ans,(j-i)*min(height[i],height[j]))
        return ans
# @lc code=end

