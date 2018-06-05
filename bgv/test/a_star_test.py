from a_star import a_star, Node


class VehicleState(Node):
    def __init__(self, x, y, children=[]):
        Node.__init__(self, children)
        self.x = x
        self.y = y


class TestAStar(object):
    def test_single_node(self):
        start = VehicleState(0, 0)
        end = start

        path_actual = a_star(start, end)[0]
        path_expected = [start]
        assert path_expected == path_actual

    def test_two_nodes_no_solution(self):
        start = VehicleState(0, 0)
        end = VehicleState(1, 1)

        path_actual = a_star(start, end)[0]
        path_expected = []
        assert path_actual == path_expected

    def test_two_nodes(self):

        end = VehicleState(1, 1)
        start = VehicleState(0, 0, [end])

        path_actual = a_star(start, end)[0]
        path_expected = [start, end]
        assert path_expected == path_actual

    def test_three_nodes_in_order(self):
        end = VehicleState(2, 2)
        middle = VehicleState(1, 1, [end])
        start = VehicleState(0, 0, [middle])
        graph = {start: [middle], middle: [end]}

        path_actual = a_star(start, end)[0]
        path_desired = [start, middle, end]
        assert path_desired == path_actual

    def test_three_nodes_branching(self):
        end = VehicleState(2, 2)
        alt = VehicleState(1.9, 1.9)
        start = VehicleState(0, 0, [end, alt])

        path_actual = a_star(start, end)[0]
        path_expected = [start, end]
        assert path_expected == path_actual

    def test_four_nodes_branching(self):
        end = VehicleState(2, 2)
        middle = VehicleState(-100, 0, [end])
        alt = VehicleState(1.9, 1.9)
        start = VehicleState(0, 0, [alt, middle])

        path_actual = a_star(start, end)[0]
        path_desired = [start, middle, end]
        assert path_desired == path_actual




