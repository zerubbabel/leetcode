#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        t=''
        for x in s:
            if 'A'<=x<='Z':
                t+=chr(ord(x)+32)
            else:
                t+=x
        return t
# @lc code=end

