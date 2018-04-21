import pseudo_projection as pp

class TestPseudoProjection(object):
    def test_two_points(self):
        x_c = [0, 1]
        y_c = [0, 0]
        s_c = [0, 1]
        theta_c = [0, 0]
        kappa_c = [0, 0]

        x = .5
        y = 1
        point_proj_desired = [0.5, 0, 0.5, 1.0, 0.0, 0.0]
        point_proj_actual = pp.project2curve(x_c, y_c, s_c, theta_c, kappa_c, x, y)
        assert point_proj_desired == point_proj_actual

