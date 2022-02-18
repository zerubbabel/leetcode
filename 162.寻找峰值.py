#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        i,j=-1,n-1
        while i+1<j:
            m=(i+j)//2
            if nums[m]<nums[m+1]:
                i=m
            else:
                j=m
        return j
# @lc code=end

