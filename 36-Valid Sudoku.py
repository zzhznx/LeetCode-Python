class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row, col = len(board), len(board[0])
        # check each row
        usedRow = [[0] * 9 for i in range(9)]
        # check each column
        usedCol = [[0] * 9 for i in range(9)]
        # check each box
        usedBox = [[0] * 9 for i in range(9)]

        for i in range(row):
            for j in range(col):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i // 3 * 3 + j // 3
                    if usedRow[i][num] or usedCol[j][num] or usedBox[k][num]:
                        return False
                    usedRow[i][num] = usedCol[j][num] = usedBox[k][num] = 1
        return True

solution = Solution()
print(solution.isValidSudoku([".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........", "9........"]))