import sim_kotm as kotm
import numpy as np
import numpy.testing as npt
from scipy.interpolate import interp1d


class TestSimKotm(object):
    def test_simulate_const_velocity_diagonal(self):
        psi_const = np.pi / 4
        x0 = [0, 0, psi_const]
        delta0 = 0

        t = np.array([0., 0.])
        delta = np.array([delta0, delta0])
        delta_of_t = interp1d(t, delta, kind='linear', fill_value='extrapolate')
        delta_test = delta_of_t([0.0, ])
        ti = np.linspace(0, 1, 10)
        v = 5
        s = ti * v
        x_desired = np.zeros((len(ti), 3))
        x_desired[:, 0] = s * np.cos(psi_const)
        x_desired[:, 1] = s * np.sin(psi_const)
        x_desired[:, 2] = np.ones(s.shape) * psi_const
        x_actual = kotm.simulate(x0, v, delta_of_t, ti)

        np.testing.assert_allclose(x_desired, x_actual, rtol=1e-5, atol=0)

    def test_drive_circle(self):
        x0 = [0, 0, 0]
        delta0 = np.pi/4
        v = 10

        length = 2
        radius = length / np.tan(delta0)
        t_pi_half = np.pi * radius / v
        ti = np.linspace(0, t_pi_half, 10)

        x_actual = kotm.simulate(x0, v, delta0, ti)

        npt.assert_almost_equal(np.pi, x_actual[-1][2], decimal=10)

