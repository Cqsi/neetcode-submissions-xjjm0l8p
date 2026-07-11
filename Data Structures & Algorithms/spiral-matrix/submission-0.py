class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        s = 0
        m = len(matrix)
        n = len(matrix[0])

        while len(res) < m * n:
            top = s
            bottom = m - 1 - s
            left = s
            right = n - 1 - s

            # top
            for i in range(left, right + 1):
                res.append(matrix[top][i])

            # right
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])

            # bottom
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])

            # left
            if left < right:
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])

            s += 1

        return res