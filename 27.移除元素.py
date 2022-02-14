#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            if nums[i]==val:
                cnt+=1
            else:
                nums[i-cnt]=nums[i]
        return n-cnt
# @lc code=end

