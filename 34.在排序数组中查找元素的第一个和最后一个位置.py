#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left,rihgt=-1,-1
        i,j=0,n-1
        while i<=j:
            m=(i+j)//2
            if nums[m]>=target:
                j=m-1
            else:
                i=m+1

        if i<n and target==nums[i]:left=i
        i,j=0,n-1
        while i<=j:
            m=(i+j)//2
            if nums[m]>target:
                j=m-1
            else:
                i=m+1
        if j>=0 and target==nums[j]:rihgt=j
        return [left,rihgt]
# @lc code=end

