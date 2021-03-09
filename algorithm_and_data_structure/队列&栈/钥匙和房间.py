from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        queue.append(0)
        visited = {0}
        while queue:
            room_index = queue.popleft()
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        if len(visited) == len(rooms):
            return True
        else:
            return False
