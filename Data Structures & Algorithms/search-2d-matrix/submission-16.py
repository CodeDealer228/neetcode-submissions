class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j = 0,0
        n,m = len(matrix), len(matrix[0])

        i1, i2 = 0, n-1
        while i2 > i1:
            mid = i1 + (i2 - i1)//2
            if matrix[mid][j] > target :
                i2 = mid - 1 
            elif matrix[mid][j] == target:
                l1=i2=i=mid
            else:
                i1 = mid + 1
      #  0 1  2 3 
      #  1 2 [3 5]
        
        iter_i = [i for i in range(n) if matrix[i][j]<=target]
        if iter_i:
            i = max(iter_i)
        else: i = 0

        iter_j = [j for j in range(m) if matrix[i][j]<=target]
        if iter_j:
            j = max(iter_j)
        else: j = 0
        return matrix[i][j] == target