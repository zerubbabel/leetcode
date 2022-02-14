#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        f=[0]*n
        if 1<=int(s[0])<=26:
            f[0]=1
        else:
            return 0
        
        if n>1:
            if 1<=int(s[1])<=26:
                f[1]=f[0]
            if 10<=int(s[:2])<=26:
                f[1]+=1
            for i in range(2,n):
                if 1<=int(s[i])<=26:
                    f[i]+=f[i-1]
                if 10<=int(s[i-1:i+1])<=26:
                    f[i]+=f[i-2]
        
        return f[-1]
               
# @lc code=end

