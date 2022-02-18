#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:
    s=None
    def __init__(self, nums: List[int]):
        n=len(nums)
        if n:
            self.s=[0]
            for i in range(n):
                self.s.append(nums[i]+self.s[-1])
            

    def sumRange(self, left: int, right: int) -> int:
        if len(self.s):
            return self.s[right+1]-self.s[left]
        return 0


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

