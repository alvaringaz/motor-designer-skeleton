# Put all the cool shit about the calculation, here or into a separate "module" file
# It's just basically a separate file with functions
import math


def calculate_torque(pn: float, speed: float) -> float:
    return pn * 1e3 / (speed / 60 * 2 * math.pi)
