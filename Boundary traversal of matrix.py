#Question:
#You are given a matrix of dimensions n x m. The task is to perform boundary traversal on the matrix in a clockwise manner.

#Example 1:

#Input:
#n = 4, m = 4
#matrix[][] = {{1, 2, 3, 4},
#         {5, 6, 7, 8},
#         {9, 10, 11, 12},
#         {13, 14, 15,16}}
#Output: 1 2 3 4 8 12 16 15 14 13 9 5
#Explanation:
#The matrix is:
#1 2 3 4
#5 6 7 8
#9 10 11 12
#13 14 15 16
#The boundary traversal is:
#1 2 3 4 8 12 16 15 14 13 9 5
#Example 2:

#Input:
#n = 3, m = 4
#matrrix[][] = {{12, 11, 10, 9},
#         {8, 7, 6, 5},
#         {4, 3, 2, 1}}
#Output: 12 11 10 9 5 1 2 3 4 8
#Your Task:
#Complete the function boundaryTraversal() that takes matrix, n and m as input parameters and returns the list of integers that form the boundary traversal of the matrix in a clockwise manner.#

#Expected Time Complexity: O(N + M)
#Expected Auxiliary Space: O(1)

#Constraints:
#1 <= n, m<= 1000
#0 <= matrixi <= 1000
class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        li=[]
        for i in range(m):
            li.append(matrix[0][i])
        for i in range(1,n):
            li.append(matrix[i][m-1])
        if (n>1):
            for i in range(m-2,-1,-1):
                li.append(matrix[n-1][i])
        if (m>1):
            for i in range(n-2,0,-1):
                li.append(matrix[i][0])
        return li
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
