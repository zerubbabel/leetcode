#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mm=100005
        ans,cur=0,mm
        for i in prices:
            cur=min(cur,i)
            ans=max(ans,i-cur)
        return ans
# @lc code=end

