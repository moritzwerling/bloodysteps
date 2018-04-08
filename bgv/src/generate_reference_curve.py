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

    # ... and its first ...
    x_diff = interpolate.splev(s_sampled, sp_x, der=1)
    y_diff = interpolate.splev(s_sampled, sp_y, der=1)

    # ... and its second derivative ...
    x_ddiff = interpolate.splev(s_sampled, sp_x, der=2)
    y_ddiff = interpolate.splev(s_sampled, sp_y, der=2)

    # delta_s = sqrt(delta_x² + delta_y²)
    s_curve = np.concatenate((np.array([0]), np.cumsum(np.sqrt(np.diff(x_curve) ** 2 + np.diff(y_curve) ** 2))))

    # tan(theta) = dy/dx = (dy/ds) / (dx/ds)
    theta_curve = np.arctan2(y_diff, x_diff)

    # kappa = (x'y'' - y'x'')/(x'² + y'²)^(3/2)
    kappa_curve = (x_diff * y_ddiff - y_diff * x_ddiff) / (x_diff**2 + y_diff**2)**(3/2)

    return {'s': s_curve, 'x': x_curve, 'y': y_curve, 'theta': theta_curve, 'kappa': kappa_curve}
