#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            y=target-nums[i]
            if y in d:
                return [d[y],i]
            else:
                d[nums[i]]=i
            
# @lc code=end

