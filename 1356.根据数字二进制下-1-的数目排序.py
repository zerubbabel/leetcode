#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
from operator import itemgetter


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n=len(arr)
        
        def countOne(x):
            s=0
            while x:
                s+=x%2
                x//=2
            return s
        b=[]
        for i in range(n):
            b.append((countOne(arr[i]),arr[i],i))

        
        b=sorted(b,key=itemgetter(0,1))
        
        ans=[]
        for x in b:
            ans.append(arr[x[2]])
        return ans
# @lc code=end

