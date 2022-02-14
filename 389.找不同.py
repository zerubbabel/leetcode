#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        for x in t:
            if x not in d or d[x]==0:
                return x
            else:
                d[x]-=1
            
# @lc code=end

