#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #中心扩散法
        n=len(s)
        maxLen=1
        begin=0
        def expand(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1

        for i in range(n-1):
            oddLen=expand(i,i)
            evenLen=expand(i,i+1)
            curLen=max(oddLen,evenLen)
            curBegin=i+1-(curLen+1)//2
            if curLen>maxLen:
                maxLen=curLen
                begin=curBegin
        return s[begin:begin+maxLen]


# @lc code=end

