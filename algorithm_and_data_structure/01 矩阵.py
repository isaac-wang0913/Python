from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # BFS 广度优先遍历
        row = len(matrix)
        col = len(matrix[0])
        # 初始化一个[0][0]的阵列
        li = [[0] * col for _ in range(row)]
        # 创建一个由matrix中值为0组成的阵列
        li_zero = [(i, j) for i in range(row) for j in range(col) if matrix[i][j] == 0]
        queue = deque(li_zero)
        visited = set(li_zero)
        while queue:
            i, j = queue.popleft()
            for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= new_i < row and 0 <= new_j < col and (new_i, new_j) not in visited:
                    li[new_i][new_j] = li[i][j] + 1
                    queue.append((new_i, new_j))
                    visited.add((new_i, new_j))
        return li
