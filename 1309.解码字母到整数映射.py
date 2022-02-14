#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        t=''
        n=len(s)
        i=n-1
        while i>=0:
            if s[i]=='#':
                t=chr(int(s[i-2:i])+ord('j')-10)+t
                i-=3
            else:
                t=s[i]+t
                i-=1
        ans=''
        n=len(t)
        for x in t:
            if '1'<=x<='9':
                ans+=chr(ord(x)-ord('1')+ord('a'))
            else:
                ans+=x
        return ans

# @lc code=end

