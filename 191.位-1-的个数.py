#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        s=0
        while n:
            s+=n%2
            n//=2
        return s
# @lc code=end

