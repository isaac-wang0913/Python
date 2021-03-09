# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 广度优先遍历BFS
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        if not node:
            return node
        visited = {}
        # 克隆第一个节点并存储到哈希表中
        visited[node] = Node(node.val, [])
        queue = [node]
        while queue:
            n = queue.pop(0)
            # 遍历该节点的邻居
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # 更新当前节点的邻居列表
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
