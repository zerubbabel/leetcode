#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from pkg_resources import NullProvider


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        i,j=-1,n-1
        while i+1<j:
            m=(i+j)//2
            if nums[m]<nums[j]:
                j=m
            elif nums[i+1]<=nums[m]:
                i=m
        return nums[j]
# @lc code=end

