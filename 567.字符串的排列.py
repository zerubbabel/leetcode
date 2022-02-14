#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if m>n:return False
        d1={}
        for c in s1:
            if c in d1:
                d1[c]+=1
            else:
                d1[c]=1
        for i in range(n-m+1):
            d2={}
            for c in s2[i:i+m]:
                if c in d2:
                    d2[c]+=1
                else:
                    d2[c]=1
            if d1==d2:return True
        return False
# @lc code=end

