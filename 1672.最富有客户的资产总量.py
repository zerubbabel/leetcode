#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for x in accounts:
            ans=max(ans,sum(x))
        return ans
# @lc code=end

