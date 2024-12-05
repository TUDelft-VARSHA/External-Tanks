import numpy as np
from scipy.integrate import quad
from math import *

rho = 7850 #kg/m^3 for low steel alloy

height = [1.6, 1.2, 1.2]
half_width = [3/2, 5.26/2, 2.75/2]
length = [14, 10, 7]

g = 9.81

thick_array = []
arc_array = []
mass_array = []

for i in range(3):
    y = np.arange(0,height[i]+0.01,0.01)
    x = np.sqrt(half_width[i]**2 / height[i] * y)


    pressure = 1000*g*(height[i]-y) + 1E5 - 16236
    radius = (1+ (2*height[i] / half_width[i]**2 * x)**2 )**(3/2) * half_width[i]**2/(2*height[i])

    product = pressure*radius
    max_loc = max(product)

    thickness = max_loc / (950E6/4) * 1000
    thick_array.append(thickness)


    def dydx(x):
        return 2*height[i] / half_width[i]**2 * x
    
    def integrand(x):
        return np.sqrt(1 + dydx(x)**2)
    
    a = -half_width[i]
    b = half_width[i]

    arc_length = quad(integrand,a,b)[0]
    arc_array.append(arc_length)


    mass = arc_length * thickness/1000 * length[i] * rho
    mass_array.append(mass)

    



print(thick_array, arc_array, mass_array)