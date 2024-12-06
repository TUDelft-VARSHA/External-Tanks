import numpy as np
from scipy.optimize import minimize


A = np.array([[np.cos(38*np.pi/180), np.cos(38*np.pi/180), 1, np.cos(30.27*np.pi/180), np.cos(34.9*np.pi/180)], [np.sin(38*np.pi/180), np.sin(38*np.pi/180), 0, -np.sin(30.27*np.pi/180), np.sin(34.9*np.pi/180)], [0, 2.32*np.sin(38*np.pi/180), 0, -30.26*np.sin(30.27*np.pi/180), 31.88*np.sin(34.9*np.pi/180)], [0, 2.32*np.cos(38*np.pi/180), 28.61, 30.26*np.cos(30.27*np.pi/180), 31.88*np.cos(34.9*np.pi/180)]])  # Coefficient matrix
b = np.array([-172.32*31.88, 0, 0, -172.32*31.88**2/2])             # Load vector


R = np.linalg.lstsq(A, b, rcond=None)[0]  # Least squares solution

print(R)