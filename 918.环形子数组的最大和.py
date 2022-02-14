#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        a=[nums[0]]
        for i in range(1,n):
            a.append(a[-1]+nums[i])
        
        mm=-30005
        f=[mm]*n
        sum=nums[-1]
        f[-1]=max(sum,0)
        for i in range(n-2,0,-1):
            sum+=nums[i]
            f[i]=max(f[i+1],sum)

        ans,cur=mm,mm
        for x in nums:
            cur=max(cur+x,x)
            ans=max(ans,cur)

        for i in range(n-2):
            ans=max(a[i]+f[i+2],ans)
        return ans
# @lc code=end

