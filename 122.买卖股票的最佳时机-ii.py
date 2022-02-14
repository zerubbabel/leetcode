#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        a,b=0,-100005#no,yes
        for i in prices:
            c,d=max(a,b+i),max(b,a-i)
            a,b=c,d
        return max(c,d)

# @lc code=end

