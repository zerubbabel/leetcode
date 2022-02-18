#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m,n=len(firstList),len(secondList)
        ans=[]
        i,j=0,0
        while i<m and j<n:
            while j<n and secondList[j][0]<=firstList[i][1]:
                if secondList[j][0]<=firstList[i][0] and secondList[j][1]>=firstList[i][1]:
                    ans.append(firstList[i])
                elif secondList[j][0]>=firstList[i][0] and secondList[j][1]<=firstList[i][1]:
                    ans.append(secondList[j])
                elif secondList[j][0]>=firstList[i][0] and secondList[j][1]>=firstList[i][1]:
                    ans.append([secondList[j][0],firstList[i][1]])
                elif secondList[j][1]>=firstList[i][0] and secondList[j][0]<=firstList[i][0]:
                    ans.append([firstList[i][0],secondList[j][1]])
                j+=1
            i+=1
            j=0
        return ans
# @lc code=end

