#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        f=[0]*(amount+1)
        f[0]=1
        for i in range(n):
            for j in range(coins[i],amount+1):
                f[j]+=f[j-coins[i]]
        return f[-1]
# @lc code=end

