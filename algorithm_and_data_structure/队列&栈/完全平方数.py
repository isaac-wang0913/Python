class Solution:
    def numSquares(self, n: int) -> int:
        # 广度优先遍历BFS
        queue = [(n, 0)]
        visited = set()
        visited.add(n)
        while queue:
            cur, count = queue.pop(0)
            target = [cur - i * i for i in range(1, int(cur ** 0.5)+1)]
            for i in target:
                if i == 0:
                    count += 1
                    return count
                if i not in visited:
                    queue.append((i, count+1))
                    visited.add(i)
        return 0
