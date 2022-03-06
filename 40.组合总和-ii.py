#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
import tarfile


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates)<target:return []
        if sum(candidates)==target:return [candidates]
        a=[0]*51
        for x in candidates:
            a[x]+=1
        can=[]
        for i in range(51):
            if a[i]:
                can.append([i,a[i]])
        n=len(can)
        ans=[]
        def find(k,target,sub):
            if target==0:
                ans.append(sub)
                return
            if k==n:return
            for i in range(min(target,can[k][1])+1):
                find(k+1,target-can[k][0]*i,sub+[can[k][0]]*i)

        find(0,target,[])

        return ans
# @lc code=end

