#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n-1,1,-1):
            if nums[i]<nums[i-1]+nums[i-2]:
                return nums[i]+nums[i-1]+nums[i-2]
        return 0
# @lc code=end

