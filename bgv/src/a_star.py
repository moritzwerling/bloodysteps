# This code was adapted from
# https://stackoverflow.com/questions/4159331/python-speed-up-an-a-star-pathfinding-algorithm

import heapq


def a_star(start, end):
    open_set = set()
    open_heap = []
    closed_set = set()

    def retrace_path(c):
        path = [c]
        while c.parent is not None:
            c = c.parent
            path.append(c)
        path.reverse()
        return path

    open_set.add(start)
    open_heap.append((0, start))
    while open_set:
        current = heapq.heappop(open_heap)[1]
        if current == end:
            return retrace_path(current)
        open_set.remove(current)
        closed_set.add(current)
        for node in current.expand():
            if node not in closed_set:
                node.H = (abs(end.x - node.x)+abs(end.y-node.y))
                if node not in open_set:
                    open_set.add(node)
                    heapq.heappush(open_heap, (node.H, node))
                node.parent = current
    return []


class Node(object):
    def __init__(self, children):
        self._H = 0
        self.parent = None
        self._children = children

    def expand(self):
        return self._children

