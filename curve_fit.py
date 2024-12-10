import numpy as np
from scipy.optimize import curve_fit

# Example data (replace with your arrays)
tau = np.array([997422.5696936557, 579102.5284432409, 445859.4786007127, 381926.0766592079, 344778.1516384327, 320546.8607680125, 303440.2168899066])  # Velocities
t = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35])  # Times

def model(tau, a, b):
    return a * tau**b

params, _ = curve_fit(model, tau, t)
a, b = params

print(f"Estimated parameters: a = {a:.4f}, b = {b:.4f}")
print(f"Relationship: t = {a:.4f} * tau^{b:.4f}")