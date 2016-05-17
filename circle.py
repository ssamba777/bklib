import math

def area(radius):
    return math.pi * (radius**2)

def circumference(radius):
    return 2*math.pi*radius

def sphereSurface(radius):
    return 4.0*area(radius)

def sphereVolum(radius):
    return (4.0/3.0)*math.pi*(radius**3)

