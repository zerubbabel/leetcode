# @before-stub-for-debug-begin
from python3problem977 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k=n#start of positive
        for i in range(n):
            if nums[i]>=0:
                k=i
                break
        ans=[]
        i,j=k-1,k
        while i>=0 and j<n:
            if abs(nums[i])<nums[j]:
                ans.append(nums[i]*nums[i])
                i-=1
            else:
                ans.append(nums[j]*nums[j])
                j+=1
        while i>=0:
            ans.append(nums[i]*nums[i])
            i-=1
        while j<n:
            ans.append(nums[j]*nums[j])
            j+=1
        return ans

# @lc code=end

