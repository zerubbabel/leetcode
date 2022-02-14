#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        n=len(nums2)
        for i in range(n):
            d[nums2[i]]=i
        a=[]
        for x in nums1:
            p=d[x]
            index=-1
            for j in range(p+1,n):
                if nums2[j]>x:
                    index=nums2[j]
                    break
            a.append(index)
        return a

# @lc code=end

