class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)

        for k in range(n//2):
            left = k
            right = n-k-1
            for i in range(left, right):
                offset = i - left
                top = matrix[left][i]
                right_val = matrix[i][right]
                bottom = matrix[right][right-offset]
                left_val = matrix[right-offset][left]

                matrix[i][right] = top
                matrix[right][right-offset] = right_val
                matrix[right-offset][left] = bottom
                matrix[left][i] = left_val