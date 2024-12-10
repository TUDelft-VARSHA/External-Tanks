from Constants import *
import sympy as sp
from scipy.integrate import quad
import numpy as np

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
    def __init__(self, velocity, rho):
        self.area = area_total
        self.cd = None
        self.velocity = velocity
        self.rho = rho

    def dragcalculation(self):
        self.drag = 0.5 * self.rho * self.velocity**2 * self.area * self.cd # * safetyfactor_drag
        return self.drag
    
class FrictionDrag(Drag):
    def __init__(self, velocity, rho):
        super().__init__(velocity, rho)
        self.area_ref = area_total
        self.Cf = None
        self.Re = None
        self.M = None
        self.length = sum(length)
        self.d = np.sqrt(4*area_total*np.pi)
        self.FF = None
        self.Cd0 = None
    
    def skinfrictioncoeff(self):
        self.Re = min(self.rho*self.velocity*self.length/mu, 38.21*(self.length/k)**1.053)  # for subsonic
        self.Cf = 0.455 / (np.log(self.Re)**2.58 * (1+0.144*self.M**2)**0.65)    # turbulent layer
    
    def formfactor(self):
        f = self.length / self.d   # slenderness ratio 
        self.FF = 1 + 0.35 / f          # for smooth external store
    
    def zeroliftcoeff(self):
        self.Cd0 = 1 / self.area_ref * self.Cf * self.FF * IF * area_wet



dragf = FrictionDrag(velocity=V_cruise, rho=rho_cruise)
dragf.M = M_cruise
dragf.skinfrictioncoeff()
dragf.formfactor()
dragf.zeroliftcoeff()
print(dragf.Cd0)

# Initial drag calculation
dragcalc = Drag(V_cruise, rho_cruise)
dragcalc.cd = dragf.Cd0 + cd0_ac
drag_force = dragcalc.dragcalculation()

print(f"Drag force: {drag_force}")