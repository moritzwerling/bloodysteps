from a_star import a_star, Node


class VehicleState(Node):
    def __init__(self, x, y):
        Node.__init__(self)
        self.x = x
        self.y = y


class TestAStar(object):
    def test_single_node(self):
        start = VehicleState(0, 0)
        end = start
        graph = {start: []}

        path_actual = a_star(graph, start, end)
        path_desired = [start]
        assert path_desired == path_actual

    def test_two_nodes_no_solution(self):
        start = VehicleState(0, 0)
        end = VehicleState(1, 1)
        graph = {start: []}

        path_actual = a_star(graph, start, end)
        path_desired = []
        assert path_desired == path_actual

    def test_two_nodes(self):
        start = VehicleState(0, 0)
        end = VehicleState(1, 1)
        graph = {start: [end]}

        path_actual = a_star(graph, start, end)
        path_desired = [start, end]
        assert path_desired == path_actual

    def test_three_nodes_in_order(self):
        start = VehicleState(0, 0)
        middle = VehicleState(1, 1)
        end = VehicleState(2, 2)
        graph = {start: [middle], middle: [end]}

        path_actual = a_star(graph, start, end)
        path_desired = [start, middle, end]
        assert path_desired == path_actual

    def test_three_nodes_branching(self):
        start = VehicleState(0, 0)
        alt = VehicleState(1.9, 1.9)
        end = VehicleState(2, 2)
        graph = {start: [alt, end]}

        path_actual = a_star(graph, start, end)
        path_desired = [start, end]
        assert path_desired == path_actual

    def test_four_nodes_branching(self):
        start = VehicleState(0, 0)
        middle = VehicleState(-100, 0)
        end = VehicleState(2, 2)
        alt = VehicleState(1.9, 1.9)
        graph = {start: [alt, middle], alt: [], middle: [end]}

        path_actual = a_star(graph, start, end)
        path_desired = [start, middle, end]
        assert path_desired == path_actual




