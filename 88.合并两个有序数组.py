#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k=0,0,0
        a=nums1[:m]
        while i<m and j<n:
            if a[i]>nums2[j]:
                nums1[k]=nums2[j]
                j+=1
            else:
                nums1[k]=a[i]
                i+=1
            k+=1
        while i<m:
            nums1[k]=a[i]
            k+=1
            i+=1
        while j<n:
            nums1[k]=nums2[j]
            k+=1
            j+=1
        

            

# @lc code=end

