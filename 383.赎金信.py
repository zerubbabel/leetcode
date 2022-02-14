#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for x in magazine:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        for x in ransomNote:
            if x not in d or d[x]==0:
                return False
            else:
                d[x]-=1
        return True
# @lc code=end

