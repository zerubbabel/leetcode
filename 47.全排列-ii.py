#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        a=[0]*21
        for x in nums:
            a[x+10]+=1
        b=[]
        for i in range(21):
            if a[i]:
                b.append([i-10,a[i]])
        ans=[]
        
        def find(k,n,sub):
            if k==n:
                ans.append(sub)
                return
            for i in range(len(b)):
                if b[i][1]:
                    b[i][1]-=1
                    find(k+1,n,sub+[b[i][0]])
                    b[i][1]+=1
        find(0,n,[])
        return ans
# @lc code=end

