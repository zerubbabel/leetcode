#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i,j=0,n-1
        while i<=j:
            m=(i+j)//2
            if nums[m]==target:return m
            if i<=m-1 and nums[i]<=nums[m-1]:
                if target<=nums[m-1] and target>=nums[i]:
                    j=m-1
                else:
                    i=m+1
            else:
                if m+1<=j and target>=nums[m+1] and target<=nums[j]:
                    i=m+1
                else:
                    j=m-1
        return -1

# @lc code=end

