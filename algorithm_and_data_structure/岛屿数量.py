class Solution:
    def numIslands(self, grid):
        # 递归  深度优先遍历 DFS
        # 时间复杂度：O(m * n)
        # 空间复杂度：O(m * n)
        # def dfs(grid, i, j):
        #     if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
        #         return
        #     grid[i][j] = '0'
        #     dfs(grid, i-1, j)
        #     dfs(grid, i+1, j)
        #     dfs(grid, i, j-1)
        #     dfs(grid, i, j+1)
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             dfs(grid, i, j)
        #             count += 1
        # return count

        # 广度优先遍历BFS
        def bfs(grid, i, j):
            queue = [[i,j]]
            while queue:
                [i,j] = queue.pop(0)
                if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == "1":
                    grid[i][j] = "0"
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(grid, i, j)
                    count += 1
        return count
