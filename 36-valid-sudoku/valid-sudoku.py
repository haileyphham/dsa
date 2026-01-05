class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        row_sets = [set() for _ in range(length)]
        col_sets = [set() for _ in range(length)]
        box_sets = [set() for _ in range(length)]

        for r in range(length):
            for c in range(length):
                if board[r][c] == ".":
                    continue
    
                if board[r][c] in row_sets[r]:
                    return False
                row_sets[r].add(board[r][c])

                if board[r][c] in col_sets[c]:
                    return False
                col_sets[c].add(board[r][c])

                if board[r][c] in box_sets[(r // 3) * 3 + (c // 3)]:
                    return False
                box_sets[(r // 3) * 3 + (c // 3)].add(board[r][c])
        return True


        