#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        f=[0]*(target+1)
        f[0]=1
        for j in range(1,target+1):
            for i in range(n):
                if j>=nums[i]:
                    f[j]+=f[j-nums[i]]
        
        return f[-1]
# @lc code=end

