import sim_dotm as dotm
import numpy as np
from numpy.testing import assert_array_equal


def test_fun():
    x, y, psi, beta, r = 0, 0, 0, 0, 0
    t = 0
    v = 10
    state_x = [x,y,psi,beta,r]
    state_x_dot = dotm.fun(state_x,v,t)
    assert(state_x_dot == [0,0,0,0,0])


def test_simulate():
    x0 = []
    delta_t = 0.01
    n_steps = 100
    x_actual = dotm.simulate(x0, delta_t, n_steps)
    x_desired = np.zeros((5,n_steps))
    assert_array_equal(x_actual, x_desired)