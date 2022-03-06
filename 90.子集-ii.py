#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        def find(k,n,sub):
            if k==n:
                if sub not in ans:
                    ans.append(sub)
                return
            find(k+1,n,sub)
            find(k+1,n,sub+[nums[k]])
        find(0,n,[])
        return ans
# @lc code=end

