#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        f=[1]*n
        
        def find(k):
            f[k]=0
            for i in range(n):
                if i!=k and f[i] and isConnected[k][i]:
                    find(i)
        ans=0
        for i in range(n):
            if f[i]:
                find(i)
                ans+=1
        return ans
# @lc code=end

