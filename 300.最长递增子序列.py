#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        f=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    f[i]=max(f[i],f[j]+1)
        return max(f)
# @lc code=end

