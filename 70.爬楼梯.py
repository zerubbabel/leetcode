#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:return n
        a,b=1,2
        for i in range(3,n+1):
            c=a+b
            a,b=b,c
        return c
# @lc code=end

