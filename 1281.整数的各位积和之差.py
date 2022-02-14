#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul,sum=1,0
        while n:
            r=n%10
            mul*=r
            sum+=r
            n//=10
        return mul-sum
# @lc code=end

