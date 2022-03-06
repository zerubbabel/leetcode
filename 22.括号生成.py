#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        ans=[]
        def find(k,n,v,s):
            if k==2*n:
                ans.append(s)
                return 
            if v>k-v:find(k+1,n,v,s+')')#左括号多时
            if v<n:find(k+1,n,v+1,s+'(')#左括号还不足时

        find(0,n,0,'')
        return ans

# @lc code=end

