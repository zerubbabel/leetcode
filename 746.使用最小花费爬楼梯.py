#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        if n<2:return 0
        a,b=0,0
        for i in range(2,n+1):
            c=min(a+cost[i-2],b+cost[i-1])
            a,b=b,c
        return c
# @lc code=end

