from scipy.integrate import odeint
import sim_kotm as kotm
import kinematic_control as kc
import pseudo_projection as pro


class KotmClosedLoop(object):
    def __init__(self, initial_condition, curve):
        self.x0 = initial_condition
        self.curve = curve

    def simulate(self, t_vector):
        x = odeint(self._f_system_dynamics, self.x0, t_vector)
        return x

    def _f_system_dynamics(self, x_, t):
        x, y, psi = x_
        _, _, _, d, theta_r, kappa_r = \
            pro.project2curve(self.curve['s'], self.curve['x'], self.curve['y'], self.curve['theta'], self.curve['kappa'],
                              x, y)
        delta = kc.feedback_law(d, psi, theta_r, kappa_r)
        v = 1  # const velocity
        x_dot = kotm.fun(x_, t, v, delta)
        return x_dot



