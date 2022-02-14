#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for x in nums:
            if x in d:
                del d[x]
            else:
                d[x]=1
        return list(d.keys())[0]
# @lc code=end

