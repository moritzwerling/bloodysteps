from numpy import linalg as LA
import numpy as np
import kinematic_control as kc


def project2curve(s_c, x_c, y_c, theta_c, kappa_c, x, y):
    p1 = [x_c[0], y_c[0]]
    p2 = [x_c[1], y_c[1]]
    theta1 = theta_c[0]
    theta2 = theta_c[1]
    s1 = s_c[0]
    s2 = s_c[1]
    mindex = 1

    px_, lambda_, sign = pseudo_projection([x, y], p1, p2, theta1, theta2)
    x_p = px_[0]
    y_p = px_[1]

    d = sign * np.sqrt((x_p - x)**2 + (y_p - y)**2)
    s_p = lambda_ * s2 + (1.0 - lambda_) * s1
    kappa1 = kappa_c[mindex - 1]
    kappa2 = kappa_c[mindex]
    delta_theta = theta2 - theta1
    delta_theta = kc.normalize_angle(delta_theta)
    theta_p = theta1 + lambda_ * delta_theta
    theta_p = kc.normalize_angle(theta_p)
    kappa_p = lambda_ * kappa2 + (1.0 - lambda_) * kappa1;

    return [px_[0], px_[1], s_p, d, theta_p, kappa_p]


def pseudo_projection(x, p1, p2, theta1, theta2):
    delta = np.array(p2) - np.array(p1)
    l = LA.norm(delta)

    # transform so that origin is p1 oriented to p2
    alpha = np.arctan2(delta[1], delta[0])
    sin_ = np.sin(-alpha)
    cos_ = np.cos(-alpha)
    R = np.array([[cos_, -sin_],
                  [sin_,  cos_]])
    x_ = np.dot(R, (np.array(x)-np.array(p1)))
    m1 = np.tan(theta1-alpha)
    m2 = np.tan(theta2-alpha)
    devi = (m1 - m2) * x_[1] + l
    if abs(devi) > 0.001:
        lambda_ = (m1 * x_[1] + x_[0]) / devi
    else:
        lambda_ = .5

    px = lambda_ * np.array(p2) + (1.0-lambda_) * np.array(p1)

    sgn = 0
    if x_[1] > 0:
        sgn = 1
    elif x_[1] < 0:
        sgn = -1

    return [px, lambda_, sgn]



