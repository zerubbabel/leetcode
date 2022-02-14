#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        f=[1000005]*(amount+1)
        f[0]=0
        for i in range(n):
            for j in range(coins[i],amount+1):
                f[j]=min(f[j],f[j-coins[i]]+1)
        if f[amount]==1000005:return -1
        return f[amount]

# @lc code=end

