# https://leetcode.com/problems/keys-and-rooms/description/

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        rooms_to_visit = [0]
        while rooms_to_visit:
            room_number = rooms_to_visit.pop()
            visited.add(room_number)
            for key in rooms[room_number]:
                if key not in visited:
                    rooms_to_visit.append(key)
                    if len(visited) == len(rooms):
                        return True
        return len(visited) == len(rooms)
