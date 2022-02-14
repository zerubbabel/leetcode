#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[]
        for i in range(n):
            t=[0,0,0]
            dp.append(t)
        dp[0]=[-prices[0],0,0]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][2]-prices[i]) #有股票
            dp[i][1]=dp[i-1][0]+prices[i]
            
            dp[i][2]=max(dp[i-1][1],dp[i-1][2])
            
        return max(dp[-1])
# @lc code=end

