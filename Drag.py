from Constants import *
import sympy as sp
from scipy.integrate import quad


# Define the variable
x = sp.Symbol('x')
height1 = 1.6
height2 = 1.2
width1 = 3
width2 = 5.26

intersec1 = -0.862563
intersec2 = 0.862563

a1 = height1 / (width1 / 2) ** 2
a2 = height2 / (width2 / 2) ** 2

def f1(x):
    p1 = a1 * x**2 -height1
    p = -p1
    return p

def f2(x):
    p2 = a2 * x**2 - height2
    p = -p2
    return p

I1, error1 = quad(f1, (-width2/2), intersec1)
I2, error2 = quad(f2, intersec1, intersec2)
I3, error3 = quad(f1, intersec2, (width2/2))
area_total = abs(I1) + abs(I2) + abs(I3)
print(area_total)

# Drag Calculation Class
class Drag:
    def __init__(self, area, cd, velocity, rho):
        self.area = area
        self.cd = cd
        self.velocity = velocity
        self.rho = rho

    def dragcalculation(self):
        self.drag = 0.5 * self.rho * self.velocity**2 * self.area * self.cd * safetyfactor_drag
        return self.drag
    

# Replace with actual values
dragcalc = Drag(area_total, Cd, V_cruise, rho_cruise)
drag_force = dragcalc.dragcalculation()

print(f"Drag force: {drag_force}")
