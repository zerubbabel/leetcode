#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        
        for i in range(n):
            if d[s[i]]==1:
                return i
        return -1
# @lc code=end

