#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n=len(s1)
        a=[]
        for i in range(n):
            if s1[i]!=s2[i]:
                a.append(i)
        if len(a)==0 or len(a)==2 and s1[a[0]]==s2[a[1]] and s1[a[1]]==s2[a[0]]:
            return True
        else:
            return False 
# @lc code=end

