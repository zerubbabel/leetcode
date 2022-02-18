#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-2):
            left,right=i+1,n-1
            target=-nums[i]
            while left<right:
                if nums[left]+nums[right]==target:
                    t=[nums[i],nums[left],nums[right]]
                    if t not in ans:
                        ans.append(t)
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        return ans
# @lc code=end

