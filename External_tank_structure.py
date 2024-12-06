from math import *
import numpy as np

# W_water = 100000 #kg
# W_tank = 10000 #Kg
# f_cap = 659 #kg/m^3

# A_t1 = 42 #m^2
# A_t2 = 52.6 #m^2
# A_t3 = 19.25 #m^2
# A_tot = A_t1 + A_t2 + A_t3

# m_t1 = 44800 #kg
# m_t2 = 42080 #kg
# m_t3 = 15400 #kg
# m_tot = m_t1 + m_t2 + m_t3


# Area_kg = A_tot/m_tot
# A_Kg = Area_kg
# Kg_area = m_tot/A_tot
# Kg_A = Kg_area

# # print(kg_A)
# # print(A_Kg)


# A_ext = Kg_A/f_cap
# print(A_ext)

# #for every tank 1.36324 times more surface area in structural support is needed. 

# A_1 = A_ext * A_t1
# A_2 = A_ext * A_t2
# A_3 = A_ext * A_t3
# print(A_1, A_2, A_3)

# #Area that is needed outside of the surface area to support the external tank
# A_diff1 = A_1 - A_t1
# A_diff2 = A_2 - A_t2
# A_diff3 = A_3 - A_t3


# A_fus = 7.14 * 53.94

# if (A_1 + A_2 + A_3) <= A_fus:
#     print('Fuselage area is sufficient')

import numpy as np

def hoop_stress_calculation(
    tank_weight,  # in Newtons (N)
    drag_force,  # in Newtons (N)
    acceleration,  # in m/s^2
    hoop_radius,  # in meters (m)
    hoop_thickness,  # in meters (m)
    material_yield_strength,  # in Pascals (Pa)
    safety_factor  # dimensionless
):
    """
    Calculate the stresses on a fuselage hoop due to an external tank.
    """

    # Cross-sectional area of the hoop
    hoop_area = 2 * np.pi * hoop_radius * hoop_thickness

    # Total load on the hoop (static and dynamic)
    total_load = tank_weight 

    # Axial stress on the hoop
    axial_stress = total_load / hoop_area

    # Longitudinal stress on the hoop
    longitudinal_stress = (total_load * hoop_radius)/ hoop_thickness

    # Maximum allowable stress
    allowable_stress = material_yield_strength / safety_factor

    # Safety check
    is_safe = axial_stress <= allowable_stress

    # Print results
    print("=== Hoop Stress Calculation ===")
    print(f"Total Load: {total_load:.2f} N")
    print(f"Hoop Cross-sectional Area: {hoop_area:.6f} m^2")
    print(f"Axial Stress: {axial_stress:.2f} Pa")
    print(f"Longitudinal Stress: {longitudinal_stress:.2f} Pa")
    print(f"Allowable Stress (with FoS): {allowable_stress:.2f} Pa")
    print(f"Is the design safe? {'Yes' if is_safe else 'No'}")
    

    return {
        "total_load": total_load,
        "axial_stress": axial_stress,
        "allowable_stress": allowable_stress,
        "is_safe": is_safe
    }


# Example: Modify these values for your scenario
tank_weight = 1079100  # N (approximately 110 ton)
drag_force = 5000  # N
acceleration = 2.5  # m/s^2 (e.g., during turbulence or maneuver)
hoop_radius = 3.57 # m
hoop_thickness = 0.02  # m
material_yield_strength = 450e6  # Pa (e.g., Aluminum 7075)
safety_factor = 2.0  # dimensionless

# Run the calculation
results = hoop_stress_calculation(
    tank_weight,
    drag_force,
    acceleration,
    hoop_radius,
    hoop_thickness,
    material_yield_strength,
    safety_factor
)




