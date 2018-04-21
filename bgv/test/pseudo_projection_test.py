import numpy as np
import pseudo_projection as pp
import pytest


class TestPseudoProjection(object):

    #@pytest.mark.skip(reason="no way of currently testing this")
    def test_two_points(self):
        x_c = [0, 1]
        y_c = [0, 0]
        s_c = [0, 1]
        theta_c = [0, 0]
        kappa_c = [0, 0]

        x = .5
        y = 1
        proj_desired = [0.5, 0, 0.5, 1.0, 0.0, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        assert proj_desired == proj_actual

    def test_two_points_diagonal(self):
        x_c = [0, 1]
        y_c = [0, 1]
        s_c = [0, np.sqrt(2)]
        theta_c = [np.pi/4, np.pi/4]
        kappa_c = [0, 0]

        x = 0.
        y = 1.
        proj_desired = [0.5, 0.5, 0.5*np.sqrt(2), 0.5*np.sqrt(2), np.pi/4, 0.0]
        proj_actual = pp.project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y)
        np.testing.assert_allclose(proj_desired, proj_actual)



