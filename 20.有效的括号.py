#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for x in s:
            if x in '([{':
                a.append(x)
            else:
                if len(a)==0:
                    return False
                else:
                    y=a.pop()
                    if not(x==')' and y=='(' or x==']' and y=='[' or x=='}' and y=='{'):
                        return False
        return len(a)==0

# @lc code=end

