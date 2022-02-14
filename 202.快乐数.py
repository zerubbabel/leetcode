#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def convert(x):
            s=0
            while x:
                s+=(x%10)**2
                x//=10
            return s
        d=[]
        while n!=1 and n not in d:
            d.append(n)
            n=convert(n)
        return n==1
# @lc code=end

