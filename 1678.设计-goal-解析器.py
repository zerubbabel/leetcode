#
# @lc app=leetcode.cn id=1678 lang=python3
#
# [1678] 设计 Goal 解析器
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        s=''
        n=len(command)
        i=0
        while i<n:
            if command[i]=='G':
                s+='G'
                i+=1
            elif command[i]=='(' and command[i+1]==')':
                s+='o'
                i+=2
            else:
                s+='al'
                i+=4
        return s
# @lc code=end

