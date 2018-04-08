import numpy as np
import kinematic_control as kc


def test_normalize_angle():
    assert kc.normalize_angle(0) == 0
    assert kc.normalize_angle(2*np.pi) == 0
    np.testing.assert_almost_equal(kc.normalize_angle(2*np.pi + 0.1), 0.1, decimal=10)
    np.testing.assert_almost_equal(kc.normalize_angle(2*np.pi - 0.1), -0.1, decimal=10)
    np.testing.assert_almost_equal(kc.normalize_angle(np.pi + 0.1), -np.pi + 0.1, decimal=10)
