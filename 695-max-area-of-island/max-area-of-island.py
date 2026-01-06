class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        same as number of islands but instead of counting how many islands we want to every time we visit a connecting item, count +=1

        and in the place where we would have counted, now get get max_area
        '''
        visited = set()
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if (r<0 or r>=rows or
                c<0 or c>=cols or
                grid[r][c]==0 or 
                (r,c) in visited):
                return 0
            visited.add((r,c))
            count = 1
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curr_area = dfs(r,c)
                    max_area = max(max_area, curr_area)
        return max_area
        