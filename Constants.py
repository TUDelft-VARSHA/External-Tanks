area_front = 5.399                                      #   [m]         biggest frontal area
Cd = 1.5                                                #   [-]         drag coefficient estimation
V_cruise = 900 / 3.6                                    #   [m/s]       cruise speed
rho_cruise = 0.01841                                    #   [kg/m3]     cruise density

g = 9.81
name = ['Tank 1', 'Tank 2', 'Tank 3']
height = [1.6, 1.2, 1.2]
half_width = [3/2, 5.26/2, 2.75/2]
length = [14, 10, 7]

materials_data = {
    "Low carbon steel": {"yield_pa": 325 * 1e6, "density_kgm3": 7850, "price_usdkg": 0.55},
    "Low alloy steel": {"yield_pa": 950 * 1e6, "density_kgm3": 7850, "price_usdkg": 0.59},
    "Stainless steel": {"yield_pa": 585 * 1e6, "density_kgm3": 7850, "price_usdkg": 6.2},
    "Aluminium alloys": {"yield_pa": 265 * 1e6, "density_kgm3": 2700, "price_usdkg": 2.2},
    "CFRP": {"yield_pa": 825 * 1e6, "density_kgm3": 1550, "price_usdkg": 39.5},
    "Glare": {"yield_pa": 382 * 1e6, "density_kgm3": 2520, "price_usdkg": 80},
}
