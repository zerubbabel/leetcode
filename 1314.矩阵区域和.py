#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        m,n=len(mat),len(mat[0])
        def getList(m,n):
            a=[]
            for i in range(m):
                t=[0]*n
                a.append(t)
            return a

        sum=getList(m,n)
        ans=getList(m,n)

        sum[0][0]=mat[0][0]
        for j in range(1,n):
            sum[0][j]=sum[0][j-1]+mat[0][j]

        for i in range(1,m):
            sum[i][0]=sum[i-1][0]+mat[i][0]
            for j in range(1,n):
                sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+mat[i][j]


        for i in range(m):
            for j in range(n):
                if i-k-1<0 and j-k-1<0:
                    ans[i][j]=sum[min(m-1,i+k)][min(n-1,j+k)]
                elif i-k-1<0:
                    ans[i][j]=sum[min(m-1,i+k)][min(n-1,j+k)]-sum[min(m-1,i+k)][j-k-1]
                elif j-k-1<0:
                    ans[i][j]=sum[min(m-1,i+k)][min(n-1,j+k)]-sum[i-k-1][min(n-1,j+k)]
                else:
                    ans[i][j]=sum[min(m-1,i+k)][min(n-1,j+k)]-sum[i-k-1][min(n-1,j+k)]-sum[min(m-1,i+k)][j-k-1]+sum[i-k-1][j-k-1]

        return ans
# @lc code=end

