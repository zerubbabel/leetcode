#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0]*n
        dp[0]=1
        p2,p3,p5=0,0,0
        for i in range(1,n):
            dp[i]=min(dp[p2]*2,dp[p3]*3,dp[p5]*5)
            if dp[i]==dp[p2]*2:
                p2+=1
            if dp[i]==dp[p3]*3:
                p3+=1
            if dp[i]==dp[p5]*5:
                p5+=1
        return dp[-1]



# @lc code=end

