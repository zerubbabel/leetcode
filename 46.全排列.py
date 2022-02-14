#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def dfs(a):
            if n==len(a):
                ans.append(a)
                return None
            for i in range(n):
                if nums[i] not in a:
                    dfs(a+[nums[i]])
        dfs([])
        return ans

# @lc code=end

