#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] 乘积为正数的最长子数组长度
#

# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mm=100005
        ans=0
        a,b=-mm,-mm#negative,positive
        c,d=-mm,-mm
        for i in nums:
            if i==0:
                c,d=-mm,-mm
            elif i>0:
                c,d=a+1,max(b+1,1)
            else:
                c,d=max(b+1,1),a+1
            ans=max(ans,d)
            a,b=c,d
        return ans
# @lc code=end

