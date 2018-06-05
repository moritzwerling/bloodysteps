import a_star


class Tile(object):
    def __init__(self, x, y):
        self.H = 0
        self.x = x
        self.y = y
        self.parent = None


class TestAStar(object):
    def test_single_node(self):
        start = Tile(0, 0)
        end = start
        graph = {}
        graph[start] = []

        path_actual = a_star.a_star(graph, start, end)
        path_desired = [start]
        assert path_desired == path_actual

    def test_two_nodes(self):
        start = Tile(0, 0)
        end = Tile(1, 1)
        graph = {}
        graph[start] = [end]

        path_actual = a_star.a_star(graph, start, end)
        path_desired = [start, end]
        assert path_desired == path_actual

    def test_three_nodes_in_order(self):
        start = Tile(0, 0)
        middle = Tile(1, 1)
        end = Tile(2, 2)
        graph = {}
        graph[start] = [middle]
        graph[middle] = [end]

        path_actual = a_star.a_star(graph, start, end)
        path_desired = [start, middle, end]
        assert path_desired == path_actual

    def test_three_nodes_branching(self):
        start = Tile(0, 0)
        alt = Tile(1.9, 1.9)
        end = Tile(2, 2)
        graph = {}
        graph[start] = [alt, end]

        path_actual = a_star.a_star(graph, start, end)
        path_desired = [start, end]
        assert path_desired == path_actual

    def test_four_nodes_branching(self):
        start = Tile(0, 0)
        middle = Tile(-100, 0)
        end = Tile(2, 2)
        alt = Tile(1.9, 1.9)
        graph = {}
        graph[start] = [alt, middle]
        graph[alt] = []
        graph[middle] = [end]

        path_actual = a_star.a_star(graph, start, end)
        path_desired = [start, middle, end]
        assert path_desired == path_actual




