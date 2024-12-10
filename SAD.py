import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.optimize import curve_fit

#Part 1: Constants
p0 = 101325
p_atm = 16236 #at 43,000ft
t = 0.2 #radial thickness
thick = 0.02 #longitudinal thickness
r = 7.14/2 #outer radius of fuselage
spacing_hoops = 0.5
rho_hoops = 2780 #Titanium 
m_tank1 = 415.517 + 237.92 + 65.79
V_tank1 = 44.8
l_tank1 = 14
m_tank2 = 309.11 + 345.68 + 45.72
V_tank2 = 42.08
l_tank2 = 10
m_tank3 = 127.367 + 32.86 + 17.25
V_tank3 = 15.4
l_tank3 = 7
m_fus = 77000 #kg
l_fus = 53.94
g = 9.81
l_wing = 17.7 #m
rho_water = 1000


def calculations(tanks):
    #Part 2: Cross-section properties
    I_xx = 1/8 * np.pi * t * (2*r-t)**3
    Q_xx = 4/3 * r * (r-1/2*t)*t

    #Part 3: Pressure stresses
    delta_p = p0 - p_atm
    sigma_hoop = delta_p * (r - 1/2 * t)
    sigma_long = 1/2 * sigma_hoop


    #Part 4: Shear/Moment diagrams

    '''Distributed weights'''
    w_fus = m_fus * g / l_fus 
    w_1 = (m_tank1 + V_tank1 * rho_water) * g / l_tank1 
    w_2 = (m_tank2 + V_tank2 * rho_water) * g  / l_tank2 
    w_3 = (m_tank3 + V_tank3 * rho_water) * g  / l_tank3

    if tanks: #Fuselage with tanks
        w_w = ((m_tank1 + m_tank2 + m_tank3) + (V_tank1 + V_tank2 + V_tank3) * rho_water) * g / l_wing + m_fus * g / l_wing

        def function_1(w_fus=w_fus):
            return -w_fus 

        def function_2(w_fus=w_fus, w_1=w_1):
            return (-w_fus - w_1)

        def function_3(w_fus=w_fus, w_1=w_1, w_w=w_w):
            return (-w_fus - w_1 + w_w)

        def function_4(w_fus=w_fus, w_2=w_2, w_w=w_w):
            return (-w_fus - w_2 + w_w)

        def function_5(w_fus=w_fus, w_3=w_3, w_w=w_w):
            return (-w_fus - w_3 + w_w)

        def function_6(w_fus=w_fus, w_3=w_3):
            return (-w_fus - w_3)
        
    else: #Fuselage without tanks (normal)
        w_w = (m_fus) * g / l_wing
        def function_1(w_fus=w_fus):
            return -w_fus 

        def function_2(w_fus=w_fus):
            return (-w_fus)

        def function_3(w_fus=w_fus, w_w=w_w):
            return (-w_fus + w_w)

        def function_4(w_fus=w_fus, w_w=w_w):
            return (-w_fus + w_w)

        def function_5(w_fus=w_fus, w_w=w_w):
            return (-w_fus + w_w)

        def function_6(w_fus=w_fus):
            return (-w_fus)

    x = np.arange(0, 53.94+0.01, 0.01)

    #Shear diagram
    def combined_shear(x):
            if 0 <= x < 7.5:
                return function_1()*x
            elif 7.5 <= x < 15.4:
                return function_2()*(x-7.5) + function_1()*7.5
            elif 15.4 < x < 21.5:
                return function_3()*(x-15.4) + function_2()*7.9 + function_1()*7.5
            elif 21.5 < x < 31.5:
                return function_4()*(x-21.5) + function_3()*7.5 + function_2()*7.9 + function_1()*7.5
            elif 31.5 < x < 33.1:
                return function_5()*(x-31.5) + function_4()*10 + function_3()*7.5 + function_2()*7.9 + function_1()*7.5
            elif 33.1 <= x < 38.5:
                return function_6()*(x-33.1) + function_5()*1.6 + function_4()*10 + function_3()*7.5 + function_2()*7.9 + function_1()*7.5
            elif 38.5 <= x < 53.94:
                return function_1()*(x-38.5) + function_6()*5.4 + function_5()*1.6 + function_4()*10 + function_3()*7.5 + function_2()*7.9 + function_1()*7.5
            else:
                return 0 

    shear_force = []

    for el in x:
        shear = combined_shear(el)
        shear_force.append(shear)

    tau_shear = np.max(np.abs(shear_force)) * Q_xx / (I_xx * t) #Most constraining


    #Moment diagram
    def combined_moment(x):
            if 0 <= x < 7.5:
                return function_1()*x**2 / 2
            elif 7.5 <= x < 15.4:
                return function_2()*(x-7.5)**2 / 2 + function_1()*7.5**2 / 2
            elif 15.4 < x < 21.5:
                return function_3()*(x-15.4)**2 / 2 + function_2()*7.9**2 / 2 + function_1()*7.5**2 / 2
            elif 21.5 < x < 31.5:
                return function_4()*(x-21.5)**2 / 2 + function_3()*7.5**2 / 2 + function_2()*7.9**2 / 2 + function_1()*7.5**2 / 2
            elif 31.5 < x < 33.1:
                return function_5()*(x-31.5)**2 / 2 + function_4()*10**2 / 2 + function_3()*7.5**2 / 2 + function_2()*7.9**2 / 2 + function_1()*7.5**2 / 2
            elif 33.1 <= x < 38.5:
                return function_6()*(x-33.1)**2 / 2 + function_5()*1.6**2 / 2 + function_4()*10**2 / 2 + function_3()*7.5**2 / 2 + function_2()*7.9**2 / 2 + function_1()*7.5**2 / 2
            elif 38.5 <= x < 53.94:
                return function_1()*(x-38.5)**2 / 2 + function_6()*5.4**2 / 2 + function_5()*1.6**2 / 2 + function_4()*10**2 / 2 + function_3()*7.5**2 / 2 + function_2()*7.9**2 / 2 + function_1()*7.5**2 / 2
            else:
                return 0 

    bending_moment = []

    for el in x:
        moment = combined_moment(el)
        bending_moment.append(moment)

    sigma_moment = np.max(np.abs(bending_moment)) * r / I_xx #Most constraining


#Part 5: Mohr's circle --> combining every stress
    sigma_x = sigma_long + sigma_moment
    sigma_z = sigma_hoop
    tau_xz = tau_shear
    sigma_ave = (sigma_x + sigma_z) / 2

    tau_max = sqrt( sigma_ave**2 + tau_xz**2 ) #This is the max occuring shear stress you're designing for

    return tau_max

#Part 6: Empirical determination of new fuselage thickness
def empirical():
    sample_t = np.arange(0.01, 0.1*r+0.01, 0.01)  # sample thicknesses
    sample_tau = []
    for el in sample_t:
        t = el
        tau = calculations(0)
        sample_tau.append(tau)

    def model(tau, a, b):
        return a * tau**b

    params, _ = curve_fit(model, sample_tau, sample_t)
    a, b = params
    return b

b = empirical()
print(b)
print(t)

new_t = t / (calculations(1)/calculations(0))**(b) #Empirical formula of t = 35571020500.0769 * design_tau^-2.0111

#Part 7: New thickness and consequences for weight
extra_t = new_t - t
extra_A = 2 * np.pi * (r - t - 1/2 * extra_t) * t
n_hoops = (l_tank1 + l_tank2 + l_tank3) / spacing_hoops + 1
extra_mass = extra_A * thick * n_hoops * rho_hoops

print(extra_mass)