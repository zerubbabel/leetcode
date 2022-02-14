#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=sum(arr)
        n=len(arr)
        for length in range(3,n+1,2):
            for start in range(n-length+1):
                s+=sum(arr[start:start+length])
        return s

# @lc code=end

