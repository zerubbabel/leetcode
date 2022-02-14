#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for k in range(n-2):
            i=k
            while i+2<n and nums[i]-nums[i+1]==nums[i+1]-nums[i+2]:
                ans+=1
                i+=1
        return ans
# @lc code=end

