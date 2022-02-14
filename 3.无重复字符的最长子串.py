#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':return 0
        ans=0
        i,j=0,0
        n=len(s)
        d={}
        for i in range(n):
            if i!=0:
                del d[s[i-1]]
            while j<n and s[j] not in d:
                d[s[j]]=j
                j+=1
            ans=max(ans,j-i)
            if j==n:break
        return ans
                       
# @lc code=end

