#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt=0
        for x in nums:
            if x==0:return 0
            if x<0:
                cnt+=1
        if cnt%2:
            return -1
        else:
            return 1
# @lc code=end

