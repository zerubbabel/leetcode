#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #暴力枚举 ac
        n=len(s)
        def hw(l,r):
            i,j=l,r
            while i<j and s[i]==s[j]:
                i+=1
                j-=1
            return i>=j

        ans=1
        begin=0
        for i in range(n-1):
            for j in range(i+ans,n):
                if hw(i,j):
                    ans=j-i+1
                    begin=i
        return s[begin:begin+ans]

# @lc code=end

