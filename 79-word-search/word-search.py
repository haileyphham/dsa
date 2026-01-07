class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if( r<0 or r>=rows or
                c<0 or c>=cols or
                word[i] != board[r][c] or
                (r,c) in visited):
                return False

            visited.add((r,c))

            if ( backtrack(r+1, c, i+1) or
                 backtrack(r-1, c, i+1) or
                 backtrack(r, c+1, i+1) or
                 backtrack(r, c-1, i+1)): #reches true, return true
                return True

            visited.remove((r,c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False

        