import sim_dotm as dotm
import numpy as np
from numpy.testing import assert_almost_equal


def test_fun():
    x, y, psi, beta, r = 0, 0, 0, 0, 0
    t = 0
    v = 10
    state_x = [x,y,psi,beta,r]
    state_x_dot = dotm.fun(state_x,v,t)
    assert(state_x_dot == [0,0,0,0,0])


def test_simulate_standstill():
    x0 = [0,0,0,0,0]
    delta_t = 0.01
    ti = np.linspace(0,1,10)
    v = 0
    x_desired = np.zeros((len(ti),5))
    x_actual = dotm.simulate(x0, v, ti)
    np.testing.assert_allclose(x_desired,x_actual)


def test_simulate_const_velocity():
    x0 = [0,0,0,0,0]
    ti = np.linspace(0,1,10)
    v = 10
    x_desired = np.zeros((len(ti),5))
    x_actual = dotm.simulate(x0, v, ti)
    x_desired[:,0] = ti*v
    np.testing.assert_allclose(x_desired,x_actual,rtol=1e-5, atol=0)
