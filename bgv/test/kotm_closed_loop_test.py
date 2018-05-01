import numpy as np
import kotm_closed_loop as cl
import generate_reference_curve as ref

def test_closed_loop_straigt_without_initial_error():
    x0 = [0.0, 0.0, 0.0]
    curve = ref.generate_reference_curve([0, 10, 20, 30], [0, 0, 0, 0], 1.0)
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    sol = model.simulate(ti)
    y = sol[:, 1]
    np.testing.assert_almost_equal(0.0, y[-1])


def test_closed_loop_straight_with_initial_error():
    x0 = [0.0, .1, 0.0]
    curve = ref.generate_reference_curve([0, 10, 20, 30], [0, 0, 0, 0], 1.0)
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    sol = model.simulate(ti)
    y = sol[:, 1]
    np.testing.assert_almost_equal(0.0, y[-1], decimal=3)


def test_closed_loop_circle_without_initial_error():
    radius = 20
    x0 = [0.0, -radius, 0.0]
    curve = ref.generate_reference_curve([0, radius, 0, -radius, 0], [-radius, 0, radius, 0, radius], 1.0)
    ti = np.arange(0, 20, 0.1)
    model = cl.KotmClosedLoop(x0, curve)
    sol = model.simulate(ti)
    d = sol[:, 3]
    #np.testing.assert_almost_equal(0.0, d[-1], decimal=3)