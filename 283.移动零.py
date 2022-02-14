#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=0
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,n):
            nums[i]=0
        
# @lc code=end

