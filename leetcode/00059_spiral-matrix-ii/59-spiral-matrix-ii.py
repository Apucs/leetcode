class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start = 1
        matrix = [[0] * n for _ in range(n)]
        # print(matrix)

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = start
                start += 1
            top += 1

            for i in range(top, bottom):
                matrix[i][right - 1] = start
                start += 1
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = start
                start += 1
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = start
                start += 1
            left += 1

        return matrix
