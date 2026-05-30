class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0])

        self.m = [[0]*(c+1) for _ in range(r+1)]

        for i in range(r):
            for j in range(c):
                self.m[i+1][j+1] = (
                self.m[i][j+1]+
                self.m[i+1][j]+
                matrix[i][j]-
                self.m[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = ( self.m[row2+1][col2+1] -
                self.m[row2+1][col1] -
                self.m[row1][col2+1] +
                self.m [row1][col1] )
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)