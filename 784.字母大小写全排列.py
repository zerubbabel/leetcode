#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        n=len(s)

        def dfs(t,k):
            if k==n:
                ans.append(t)
                return None

            dfs(t+s[k],k+1)
            if 'a'<=s[k]<='z':
                dfs(t+chr(ord(s[k])-32),k+1)
            elif 'A'<=s[k]<='Z':
                dfs(t+chr(ord(s[k])+32),k+1)
        dfs('',0)
        return ans
# @lc code=end

