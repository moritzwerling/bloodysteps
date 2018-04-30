import numpy as np
from scipy.integrate import odeint
import kinematic_control as kc
import generate_reference_curve as ref


def test_normalize_angle():
    assert kc.normalize_angle(0) == 0
    assert kc.normalize_angle(2*np.pi) == 0
    np.testing.assert_almost_equal(kc.normalize_angle(2*np.pi + 0.1), 0.1, decimal=10)
    np.testing.assert_almost_equal(kc.normalize_angle(2*np.pi - 0.1), -0.1, decimal=10)
    np.testing.assert_almost_equal(kc.normalize_angle(np.pi + 0.1), -np.pi + 0.1, decimal=10)


def test_kinematic_control_law():
    # delta = feedback_law(d, psi, theta_r, kappa_r)
    assert kc.feedback_law(0, 0, 0, 0) == 0
    assert kc.feedback_law(0, 0.1, 0.1, 0) == 0
    assert kc.feedback_law(0, 0.1, 0.2, 0) > 0
    assert kc.feedback_law(0, 0.3, 0.2, 0) < 0
    assert kc.feedback_law(0.1, 0, 0, 0) < 0
    assert kc.feedback_law(-0.1, 0, 0, 0) > 0
    assert kc.feedback_law(0, 0.1, 0.1, 0.1) > 0.0
    assert kc.feedback_law(0, 0.1, 0.1, -0.1) < 0.0


def test_closed_loop_straigt_without_initial_error():
    x0 = [0.0, 0.0, 0.0]
    curve = ref.generate_reference_curve([0, 10, 20, 30], [0, 0, 0, 0], 1.0)
    ti = np.arange(0, 20, 0.1)
    sol = odeint(kc.f_closed_loop, x0, ti, (curve,))
    y = sol[:, 1]
    np.testing.assert_almost_equal(0.0, y[-1])


def test_closed_loop_straigt_with_initial_error():
    x0 = [0.0, .1, 0.0]
    curve = ref.generate_reference_curve([0, 10, 20, 30], [0, 0, 0, 0], 1.0)
    ti = np.arange(0, 20, 0.1)
    sol = odeint(kc.f_closed_loop, x0, ti, (curve,))
    y = sol[:, 1]
    np.testing.assert_almost_equal(0.0, y[-1], decimal=3)

