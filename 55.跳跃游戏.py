#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        f=[0]*n
        f[0]=1
        right=0
        for i in range(n-1):
            if f[i]:
                for j in range(right+1,min(i+nums[i]+1,n)):
                    f[j]=1
                right=max(right,i+nums[i])
            else:
                break
        return f[-1]==1
# @lc code=end

