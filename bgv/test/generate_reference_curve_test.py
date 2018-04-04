import generate_reference_curve as rc
import numpy as np


class TestGenerateReferenceCurve(object):
    def test_straight_line(self):
        x = np.arange(0, 110, 10)
        y = np.zeros(x.shape)
        delta = 1
        curve_desired = {"x": np.arange(0, 101, 1), "y": np.zeros(101)}
        curve_actual = rc.generate_reference_curve(x, y, delta)
        for key, value in curve_desired.items():
            np.testing.assert_allclose(curve_actual[key], curve_desired[key])

    def test_diagonal_line(self):
        alpha = np.pi / 4.
        s = np.arange(0, 110, 10)
        x = s * np.cos(alpha)
        y = s * np.sin(alpha)
        theta = np.full(101,alpha)
        delta = 1
        s_ = np.arange(0, 101, 1)
        curve_desired = {'x': s_*np.cos(alpha), 'y': s_*np.sin(alpha), 'theta': theta}
        curve_actual = rc.generate_reference_curve(x, y, delta)
        for key, value in curve_desired.items():
            np.testing.assert_allclose(curve_actual[key], curve_desired[key], rtol=1e-7, atol=1e-7)
