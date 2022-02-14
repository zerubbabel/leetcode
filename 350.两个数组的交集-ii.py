#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n=len(nums1),len(nums2)
        a=[]
        d={}
        for x in nums1:
            if x not in d:
                d[x]=1
            else:
                d[x]+=1
        for x in nums2:
            if x in d and d[x]>0:
                a.append(x)
                d[x]-=1
        return a
# @lc code=end

