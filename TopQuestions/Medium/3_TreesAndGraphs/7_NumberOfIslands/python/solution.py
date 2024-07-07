from collections import deque

# Approach1: Use a visited grid to keep track of what cells have been visited
class Solution1(object):
    def __init__(self):
        self.grid = []
        self.visited = []
        self.rows = 0
        self.cols = 0
    
    def traverseNeighbors(self, r, c):
        q = deque()
        q.append([r,c])
        while q:
            t = q.popleft()
            i = t[0]
            j = t[1]
            # Mark current cell as visited
            self.visited[i][j] = True
            # Initialize coordinates for all 4 neighbors
            U = [i-1, j]
            D = [i+1, j]
            L = [i, j-1]
            R = [i, j+1]
            # Check if coordinates are out of bounds
            if (U[0] < 0):
                U = None
            if (D[0] >= self.rows):
                D = None
            if (L[1] < 0):
                L = None
            if (R[1] >= self.cols):
                R = None
            # Add to queue if neighbor has not been visited
            for N in [U,D,L,R]:
                if (N != None) and not (self.visited[N[0]][N[1]]) and (self.grid[N[0]][N[1]] == '1'):
                    q.append(N)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        # Initialize visited bool list
        for r in range(self.rows):
            self.visited.append([False] * self.cols)
        # Begin traversing grid
        for i in range(self.rows):
            for j in range(self.cols):
                # Begin a BFS to mark all neighbors
                if self.grid[i][j] == '1' and not self.visited[i][j] :
                    self.traverseNeighbors(i, j)
                    num += 1
        return num

# Approach #2: Use grid to keep track of what islands have been visited by marking visited ones as '0'
class Solution():
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        i = 0
        islands = 0
        while i < rows:
            j = 0
            while j < cols:
                if (grid[i][j] == '1'):
                    q = deque()
                    q.append((i,j))
                    grid[i][j] = '0'
                    while q:
                        r,c = q.popleft()
                        # Check up neighbor
                        if (r - 1 >= 0) and (grid[r-1][c] == '1'):
                            q.append((r-1,c))
                            grid[r-1][c] = '0'  # Mark as visited so it doesn't get added by a different neighbor's BFS
                        # Check down neighbor
                        if (r + 1 < rows) and (grid[r+1][c] == '1'):
                            q.append((r+1,c))
                            grid[r+1][c] = '0'  # Mark as visited so it doesn't get added by a different neighbor's BFS
                        # Check left neighbor
                        if (c - 1 >= 0)  and (grid[r][c-1] == '1'):
                            q.append((r,c-1))
                            grid[r][c-1] = '0'  # Mark as visited so it doesn't get added by a different neighbor's BFS
                        # Check right neighbor
                        if (c + 1 < cols)  and (grid[r][c+1] == '1'):
                            q.append((r,c+1))
                            grid[r][c+1] = '0'  # Mark as visited so it doesn't get added by a different neighbor's BFS
                    islands += 1
                j += 1
            i += 1
        return islands

if __name__ == '__main__':
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    grid3 = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    grids = [grid1, grid2, grid3]
    for i in range(len(grids)):
        s = Solution()
        n = s.numIslands(grids[i])
        print(f"Grid #{i+1} Number of Islands = {n}")
