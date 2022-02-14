#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return 0
        p,cnt=0,0
        while p+nums[p]<n-1:
            cnt+=1
            tp=p+1
            for j in range(p+1,min(nums[p]+p+1,n)):
                if j+nums[j]>tp+nums[tp]:
                    tp=j
            p=tp
        return cnt+1
            

# @lc code=end

