#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        s=[0]*10001
        a,b=0,0#no,yes
        c,d=a,b
        for x in nums:
            s[x]+=1
        for i in range(1,10001):
            c,d=max(a,b),a+i*s[i]#no,yes
            a,b=c,d
        return max(c,d)

# @lc code=end

