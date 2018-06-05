# This code was adapted from
# https://stackoverflow.com/questions/4159331/python-speed-up-an-a-star-pathfinding-algorithm

import heapq


def a_star(graph, start, end):
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
        start = heapq.heappop(open_heap)[1]
        if start == end:
            return retrace_path(start)
        open_set.remove(start)
        closed_set.add(start)
        for node in graph[start]:
            if node not in closed_set:
                node.H = (abs(end.x - node.x)+abs(end.y-node.y))
                if node not in open_set:
                    open_set.add(node)
                    heapq.heappush(open_heap, (node.H, node))
                node.parent = start
    return []


class Node(object):
    def __init__(self):
        self.H = 0
        self.parent = None

