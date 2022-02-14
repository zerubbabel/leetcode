#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        a,b=-1000005,0#yes,no
        c,d=a,b
        for x in prices:
            c,d=max(a,d-x),max(b,a+x-fee)
            a,b=c,d
        return max(c,d)
# @lc code=end

