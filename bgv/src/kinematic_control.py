import numpy as np


def feedback_law(d, theta_r, kappa_r, psi):
    steering_ratio = 18
    axis_distance = 2.9680
    k_0 = 0.2
    k_1 = 1.

    # Stabilization
    u = - k_0 * d - k_1 * normalize_angle(psi-theta_r)

    # Re-substitution
    delta = np.atan(axis_distance*u)
    stwa = delta*steering_ratio


def normalize_angle(angle):
    return (angle+np.pi) % (2*np.pi) - np.pi

