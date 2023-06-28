class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False]*len(rooms)
        stack = [0]
        seen[0] = True
        while stack:
            temp = stack.pop()
            for nei in rooms[temp]:
                if not seen[nei]:
                    seen[nei] = True
                    stack.append(nei)
        return all(seen)