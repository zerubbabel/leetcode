#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates)==target:return [candidates]
        ans=[]
        candidates.sort()
        def find(candidates,target,comb):
            if sum(candidates)<target:return None
            if sum(candidates)==target:
                t=comb+candidates
                t.sort()
                if t not in ans:
                    ans.append(t)
                return None
            if target==0:
                comb.sort()
                if comb not in ans:
                    ans.append(comb)
                return None
            if len(candidates)==0:
                return None
            find(candidates[:-1],target,comb)
            if target>=candidates[-1]:
                find(candidates[:-1],target-candidates[-1],comb+[candidates[-1]])

        find(candidates,target,[])
        return ans

# @lc code=end

