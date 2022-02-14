#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        f=[]#f[i]:negative,positive
        ans=1
        for i in range(n):
            f.append([1,1])
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    f[i][1]=max(f[i][1],f[j][0]+1)#nums[i]结束，与前面差值为正的最长摆动序列长度
                elif nums[i]<nums[j]:
                    f[i][0]=max(f[i][0],f[j][1]+1)
                ans=max(ans,max(f[i]))
        return ans

# @lc code=end

