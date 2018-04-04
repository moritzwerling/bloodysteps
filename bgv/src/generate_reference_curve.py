import numpy as np
from scipy import interpolate


def generate_reference_curve(xx, yy, delta):
    delta_s = np.sqrt(np.diff(xx)**2 + np.diff(yy)**2)
    chords = np.cumsum(np.concatenate([[0], delta_s]))

    # Generate non-smoothing spline for xx(s) and yy(s)
    sp_x = interpolate.splrep(chords, xx, s=0)
    sp_y = interpolate.splrep(chords, yy, s=0)

    # At every delta meter, evaluate spline...
    s_sampled = np.arange(0, max(chords)+delta, delta)
    x_curve = interpolate.splev(s_sampled, sp_x, der=0)
    y_curve = interpolate.splev(s_sampled, sp_y, der=0)

    # ... and its first derivative.
    x_diff = interpolate.splev(s_sampled, sp_x, der=1)
    y_diff = interpolate.splev(s_sampled, sp_y, der=1)

    # tan(theta) = dy/dx = (dy/ds) / (dx/ds)
    theta_curve = np.arctan2(y_diff, x_diff)

    return {'x': x_curve, 'y': y_curve, 'theta': theta_curve}
