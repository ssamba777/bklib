pi = 3.1415

def area(radius):
    return pi * (radius**2)

def circumference(radius):
    return 2*pi*radius

def sphereSurface(radius):
    return 4.0*area(radius)

def sphereVolum(radius):
    return (4.0/3.0)*pi*(radius**3)
