#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ans,t='',''
        for c in s:
            if c==' ':
                ans+=t+' '
                t=''
            else:
                t=c+t
        if t!='':
            ans+=t
        return ans
# @lc code=end

