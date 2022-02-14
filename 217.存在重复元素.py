#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for x in nums:
            if x in d:
                return True
            else:
                d[x]=1
        return False
# @lc code=end

