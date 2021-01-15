from math import pi

def radians_to_degrees(radians):
    degrees = radians*(180/pi)
    return round(degrees, 1)