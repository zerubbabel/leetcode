#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        a=[]
        for i in range(32):
            a.append(n%2)
            n//=2
        s=0
        for x in a:
            s=s*2+x
        return s        
# @lc code=end

