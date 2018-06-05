# This code was adapted from
# https://stackoverflow.com/questions/4159331/python-speed-up-an-a-star-pathfinding-algorithm

import heapq


def a_star(graph, current, end):
    open_set = set()
    open_heap = []
    closed_set = set()

    def retracePath(c):
        path = [c]
        while c.parent is not None:
            c = c.parent
            path.append(c)
        path.reverse()
        return path

    open_set.add(current)
    open_heap.append((0, current))
    while open_set:
        current = heapq.heappop(open_heap)[1]
        if current == end:
            return retracePath(current)
        open_set.remove(current)
        closed_set.add(current)
        for tile in graph[current]:
            if tile not in closed_set:
                tile.H = (abs(end.x - tile.x)+abs(end.y-tile.y))
                if tile not in open_set:
                    open_set.add(tile)
                    heapq.heappush(open_heap, (tile.H, tile))
                tile.parent = current
    return []

