#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def find(candidates,target,comb):
            if target==0:
                ans.append(comb)
                return None
            if len(candidates)==0:
                return None
            find(candidates[:-1],target,comb)
            if target>=candidates[-1]:
                find(candidates,target-candidates[-1],comb+[candidates[-1]])
        find(candidates,target,[])
        return ans
# @lc code=end

