#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        f=[0]*n
        maxlen=0
        for sub in wordDict:
            maxlen=max(maxlen,len(sub))
        for i in range(n):
            for j in range(i-1,max(-2,i-maxlen-1),-1):
                if s[j+1:i+1] in wordDict and (j<0 or f[j]==1):
                    f[i]=1
                    break
            print(f[i])
        return f[-1]==1

# @lc code=end

