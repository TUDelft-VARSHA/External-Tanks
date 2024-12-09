Cd = 0.9                                                #   [-]         drag coefficient estimation https://aerospaceweb.org/question/aerodynamics/q0231.shtml
V_cruise = 900 / 3.6                                    #   [m/s]       cruise speed
rho_cruise = 0.331985                                   #   [kg/m3]     cruise density 
V_TO = 90                                               #   [m/s]       take off speed
rho_atm = 1.224                                         #   [kg/m3]     take off density
rho_w = 1000                                            #   [kg/m3]     density of water
p_atm = 101325
p_min = 16236
safetyfactor_p = 4
safetyfactor_drag = 1.5                                   #   [-]         to add for influence on other system due to external tanks

g = 9.81
name = ['Tank 1', 'Tank 2', 'Tank 3']
height = [1.6, 1.2, 1.2]                                #   [m]         height of external tank
width = [3, 5.26, 2.75]                                 #   [m]         width of external tank
half_width = [w / 2 for w in width]                     #   [m]         half the width
length = [14, 10, 7]                                    #   [m]         length of external tank

materials_data = {
    "Low carbon steel": {"yield_pa": 325 * 1e6, "density_kgm3": 7850, "price_usdkg": 0.55},
    "Low alloy steel": {"yield_pa": 950 * 1e6, "density_kgm3": 7850, "price_usdkg": 0.59},
    "Stainless steel": {"yield_pa": 585 * 1e6, "density_kgm3": 7850, "price_usdkg": 6.2},
    "Aluminium alloys": {"yield_pa": 265 * 1e6, "density_kgm3": 2700, "price_usdkg": 2.2},
    "CFRP": {"yield_pa": 825 * 1e6, "density_kgm3": 1550, "price_usdkg": 39.5},
    "Glare": {"yield_pa": 382 * 1e6, "density_kgm3": 2520, "price_usdkg": 80},
}
