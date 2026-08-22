class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            for idx, num in enumerate(row):
                if num != ".":
                    if num in row[:idx]:
                        return False
        for i in range(9):
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in [board[k][i] for k in range(j)]:
                        return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                test = []
                for i in range(3):
                    for j in range(3):
                        if board[r + i][c + j] != ".":
                            test.append(board[r + i][c + j])

                if len(test) != len(set(test)):
                    return False
        return True