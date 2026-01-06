class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        every iteration, we up the count until we have changed all the neighbors into rotten
'''        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        count = 0
        fresh = 0
        if not grid or not grid[0]:
            return -1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh+=1
        while queue and fresh>0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0<=nr<rows and 
                        0<=nc<cols and 
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh-=1
                        queue.append((nr,nc))
            count +=1
        return count if fresh == 0 else -1








