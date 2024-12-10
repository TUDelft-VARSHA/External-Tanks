import numpy as np
from scipy.integrate import quad
from math import *

rho = 7850 #kg/m^3 for low steel alloy
yield_stress = 950E6

height = [1.6, 1.2, 1.2]
half_width = [3/2, 5.26/2, 2.75/2]
length = [14, 10, 7]

g = 9.81

thick_array = []
arc_array = []
mass_array = []
frontal_array = []
volume_array = []

for i in range(3):
    y = np.arange(0,height[i]+0.01,0.01)
    x = np.sqrt(half_width[i]**2 / height[i] * y)


    pressure = 1000*g*(height[i]-y) + 101325 - 16236
    radius = (1+ (2*height[i] / half_width[i]**2 * x)**2 )**(3/2) * half_width[i]**2/(2*height[i])

    product = pressure*radius
    max_loc = max(product)

    thickness = max_loc / (yield_stress/4) * 1000
    thick_array.append(thickness)


    def dydx(x):
        return 2*height[i] / half_width[i]**2 * x
    
    def integrand(x):
        return np.sqrt(1 + dydx(x)**2)
    
    a = -half_width[i]
    b = half_width[i]

    arc_length = quad(integrand,a,b)[0]
    arc_array.append(arc_length)


    def parabola(x):
        return height[i]/half_width[i]**2 * x**2

    frontal_area = height[i] * 2*half_width[i] - quad(parabola,a,b)[0]
    frontal_array.append(frontal_area)

    volume = frontal_area * length[i]
    volume_array.append(volume)

    mass = (arc_length * thickness/1000 * length[i] + frontal_area*thickness/1000*2) * rho
    mass_array.append(mass)

    
    


print( (np.array(mass_array) + np.array(volume_array)*1000) /np.array(length)*9.81)
print( sum((np.array(mass_array) + np.array(volume_array)*1000))*9.81 + 77000*9.81)