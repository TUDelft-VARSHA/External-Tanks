import numpy as np
from scipy.integrate import quad
from math import *
from Constants import * 
from tabulate import tabulate

thick_array = []
arc_array = []
mass_array = []
frontal_array = []
volume_array = []

class External:
    def __init__(self, height, halfwidth, length, sigma=None, name = None):
        self.height = height
        self.halfwidth = halfwidth
        self.length = length
        self.sigma = sigma
        self.volumemat = None
        self.price = None
        self.mat = None
        self.mass = None
        self.frontal_area = None
        self.arc_length = None
        self.t = None
        self.name = name

    def calculate_x(self):
        """Calculate x based on the tank's geometry."""
        self.y = np.arange(0, self.height + 0.01, 0.01)  # Array of y values
        self.x = np.sqrt(self.halfwidth**2 / self.height * self.y)  # Calculate x for each y value
        return
    
    def dydx(self, x):
        """Calculate dydx based on the geometry."""
        return 2 * self.height / self.halfwidth**2 * x

    def integrand(self, x):
        """Calculate the integrand for the arc length."""
        return np.sqrt(1 + self.dydx(x)**2)

    def parabola(self, x):
        """Calculate the parabola function for frontal area."""
        return self.height / self.halfwidth**2 * x**2

    def calculatethickness(self):
        """Calculate material thickness."""
        self.calculate_x()  # Ensure x is calculated
        pressure = rho_w * g * (self.height - self.y) + (p_atm - p_min)
        radius = (1 + (2 * self.height / self.halfwidth**2 * self.x)**2)**(3/2) * self.halfwidth**2 / (2 * self.height)
        product = pressure * radius
        max_loc = max(product)
        self.t = max_loc / (self.sigma / safetyfactor_p) 
        return self.t

    def calculate_arclength(self):
        """Calculate arc length using numerical integration."""
        self.calculate_x()  # Ensure x is calculated
        arc_length = quad(self.integrand, -self.halfwidth, self.halfwidth)[0]
        self.arc_length = arc_length
        return arc_length

    def calculate_frontalarea(self):
        """Calculate the frontal area."""
        self.calculate_x()  # Ensure x is calculated
        frontal_area = self.height * 2 * self.halfwidth - quad(self.parabola, -self.halfwidth, self.halfwidth)[0]
        self.frontal_area = frontal_area
        return frontal_area

    def calculate_volume(self):
        """Calculate the volume."""
        self.calculate_arclength()  # Ensure arc length is calculated
        self.calculate_frontalarea()  # Ensure frontal area is calculated
        self.volumemat = self.t * (self.arc_length * self.length + self.frontal_area * 2)
        return self.volumemat

# Example of running the loop
externaltanks = list()

for mat, data in materials_data.items():
    for h, w, l, n in zip(height, half_width, length, name):
        externaltank = External(height=h, halfwidth=w, length=l, sigma=data["yield_pa"], name=n)
        externaltank.calculatethickness()
        externaltank.calculate_arclength()
        externaltank.calculate_frontalarea()
        externaltank.calculate_volume()
        externaltank.mat = mat
        externaltank.mass = data["density_kgm3"] * externaltank.volumemat
        externaltank.price = data["price_usdkg"] * externaltank.mass
        externaltanks.append(externaltank)

table_externaltanks = [[tank.name, tank.mat, (tank.t)*1000, tank.mass, tank.price] for tank in externaltanks]
headers_externaltanks = ["Tank name", "Material", "Thickness [mm]", 'Mass [kg]', 'Price [$]']
print(tabulate(table_externaltanks, headers=headers_externaltanks, tablefmt="grid"))

material_totals = {}

for tank in externaltanks:
    material = tank.mat
    # If the material is already in the dictionary, update the totals
    if material in material_totals:
        material_totals[material]["mass"] += tank.mass
        material_totals[material]["price"] += tank.price
    else:
        # If the material is not in the dictionary, initialize it
        material_totals[material] = {"mass": tank.mass, "price": tank.price}

table_material_totals = [[material, totals["mass"], totals["price"]] for material, totals in material_totals.items()]
headers_material_totals = ["Material", "Total Mass [kg]", "Total Price [$]"]
print(tabulate(table_material_totals, headers=headers_material_totals, tablefmt="grid"))
