class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 哈希表
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    n = int(board[i][j])
                    box_index = i // 3 * 3 + j // 3
                    row[i][n] = row[i].get(n, 0) + 1
                    col[j][n] = col[j].get(n, 0) + 1
                    box[box_index][n] = box[box_index].get(n, 0) + 1
                    if row[i][n] > 1 or col[j][n] > 1 or box[box_index][n] > 1:
                        return False
        return True
