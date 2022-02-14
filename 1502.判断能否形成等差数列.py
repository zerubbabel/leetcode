#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n=len(arr)
        if n==2:return True
        d=arr[1]-arr[0]
        for i in range(2,n):
            if arr[i]-arr[i-1]!=d:
                return False
        return True
# @lc code=end

