"""Basic vector geometry functions."""
import math

def unit_vector(vector):
    magnitude = math.sqrt(sum(x*x for x in vector))
    if magnitude == 0:
        raise ValueError("Zero vector has no direction.")
    return tuple(x / magnitude for x in vector)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def angle_between(a, b):
    ua, ub = unit_vector(a), unit_vector(b)
    value = max(-1.0, min(1.0, dot(ua, ub)))
    return math.degrees(math.acos(value))

if __name__ == "__main__":
    print(f"Angle: {angle_between((0,0,1), (1,0,1)):.2f} degrees")
