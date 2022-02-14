#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans=[]
        def dfs(dep,a):
            if dep==k:
                ans.append(a)
                return None
            for i in range(1,n+1):
                if i not in a and (dep==0 or i>a[-1]):
                    dfs(dep+1,a+[i])
        
        dfs(0,[])
        return ans

# @lc code=end

