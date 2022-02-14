#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        d={}
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for x in t:
            if x not in d or d[x]==0:
                return False
            else:
                d[x]-=1
        return True
# @lc code=end

