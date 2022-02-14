#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def gcd(m,n):
            while n!=0:
                m,n=n,m%n
            return m
        round=gcd(n,k)

        for i in range(round):
            p=i
            buffer=nums[p]
            while p!=(i+k)%n:
                q=(p-k+n)%n
                nums[p]=nums[q]
                p=q
            nums[p]=buffer
        
# @lc code=end

