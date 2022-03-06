#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.a=nums[:]

    def reset(self) -> List[int]:
        return self.a

    def shuffle(self) -> List[int]:
        import random
        b=self.a[:]
        random.shuffle(b)
        return b


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

