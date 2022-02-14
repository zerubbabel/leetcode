#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n=len(word1),len(word2)
        L=min(m,n)
        s=''
        for i in range(L):
            s+=word1[i]+word2[i]
        return s+word1[L:]+word2[L:]
        
# @lc code=end

