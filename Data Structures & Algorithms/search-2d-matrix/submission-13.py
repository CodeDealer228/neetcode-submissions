class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,0
        n,m = len(matrix), len(matrix[0])
        iter_i = [i for i in range(n) if matrix[i][j]<=target]
        if iter_i:
            i = max(iter_i)
        else: i = 0

        iter_j = [j for j in range(m) if matrix[i][j]<=target]
        if iter_j:
            j = max(iter_j)
        else: j = 0
        return matrix[i][j] == target