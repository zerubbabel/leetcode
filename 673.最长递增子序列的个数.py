#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        f=[1]*n
        maxk=0
        #计算最长递增子序列长度
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    f[i]=max(f[j]+1,f[i])
            if f[maxk]<f[i]:maxk=i
        
        cnt=[0]*n
        cnt[0]=1
        #统计最长递增子序列个数
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and f[j]==f[i]-1:
                    cnt[i]+=cnt[j]
            if cnt[i]==0:cnt[i]=1
        ans=0
        for i in range(n):
            if f[maxk]==f[i]:ans+=cnt[i]
        return ans
# @lc code=end

