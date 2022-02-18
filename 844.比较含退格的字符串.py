#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def do(s):
            r=[]
            for x in s:
                if x=='#':
                    if len(r):
                        r.pop()
                else:
                    r.append(x)
            return r
        a=do(s)
        b=do(t)
        return a==b
# @lc code=end

