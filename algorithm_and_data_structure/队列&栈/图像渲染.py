from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # # BFS 广度优先搜索
        # if image[sr][sc] == newColor:
        #     return image
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # original_color = image[sr][sc]
        # queue = deque()
        # queue.append((sr, sc))
        # while queue:
        #     point = queue.popleft()
        #     image[point[0]][point[1]] = newColor
        #     for direction in directions:
        #         new_i = point[0] + direction[0]
        #         new_j = point[1] + direction[1]
        #         if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == original_color:
        #             queue.append((new_i, new_j))
        # return image

        # DFS 深度优先搜索
        if newColor == image[sr][sc]: return image
        stack, old = [(sr, sc)], image[sr][sc]
        while stack:
            point = stack.pop()
            image[point[0]][point[1]] = newColor
            for new_i, new_j in zip((point[0], point[0], point[0] + 1, point[0] - 1),
                                    (point[1] + 1, point[1] - 1, point[1], point[1])):
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == old:
                    stack.append((new_i, new_j))
        return image
