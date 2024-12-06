area_front = 5.399                                      #   [m]         biggest frontal area
Cd = 1.5                                                #   [-]         drag coefficient estimation
V_cruise = 900 / 3.6                                    #   [m/s]       cruise speed
rho_cruise = 0.01841                                    #   [kg/m3]     cruise density 
rho_w = 1000
p_atm = 101325
p_min = 16236
safetyfactor_p = 4
safetyfactor_drag = 2                                   #   [-]         to add for influence on other system due to external tanks

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
