class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_node = set()

        # print(matrix,"\n")

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_node.add((i,j))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 and (i,j) in zero_node:
                    row, col = i, j
                    for k in range(len(matrix)):
                        matrix[k][col] = 0
                    for k in range(len(matrix[i])):
                        matrix[row][k] = 0
