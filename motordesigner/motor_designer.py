# Put all the cool stuff about the calculations here and import it
import math


def calculate_torque(pn: float, speed: float) -> float:
    return pn * 1e3 / (speed / 60 * 2 * math.pi)
