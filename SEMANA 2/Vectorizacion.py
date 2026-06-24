import numpy as np

presiones_psi = np.array([14.7, 30.2, 55.0, 120.5, 85.0])
presiones_atm = presiones_psi * 0.068046

print(f"Presiones en psi: {presiones_psi}")
print(f"Presiones en atm: {presiones_atm}")

