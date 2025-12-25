class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c): #checking the neighbors
            if (r < 0  or
                r >= rows or 
                c < 0 or
                c >= cols or 
                grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    dfs(r, c)
                visited.add((r,c))

        return count


