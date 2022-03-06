#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        def find(cur,path):
            if cur==n-1:
                ans.append(path)
                return 
            for next in graph[cur]:
                find(next,path+[next])
        find(0,[0])
        return ans
# @lc code=end

