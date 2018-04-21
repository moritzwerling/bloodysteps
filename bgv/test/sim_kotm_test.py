import sim_kotm as kotm
import numpy as np


def test_simulate_const_velocity_diagonal():
    psi_const = np.pi / 4
    x0 = [0, 0, psi_const]
    ti = np.linspace(0, 1, 10)
    v = 5
    s = ti * v
    x_desired = np.zeros((len(ti), 3))
    x_desired[:, 0] = s * np.cos(psi_const)
    x_desired[:, 1] = s * np.sin(psi_const)
    x_desired[:, 2] = np.ones(s.shape) * psi_const
    x_actual = kotm.simulate(x0, v, ti)

    np.testing.assert_allclose(x_desired, x_actual, rtol=1e-5, atol=0)
