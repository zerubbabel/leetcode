#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def find(k,n,sub):
            if k==n:
                ans.append(sub)
                return
            find(k+1,n,sub)
            find(k+1,n,sub+[nums[k]])
        find(0,n,[])
        return ans
# @lc code=end

