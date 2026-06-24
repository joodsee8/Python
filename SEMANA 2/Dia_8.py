# Dia 8
# Autor Jose Arteaga

Temperatura_R = float(input("Ingresa la temperatura del Reactor: "))
Presion_R = float(input("Ingresa la presion en atm: "))
Nivel_T = float(input("Ingresa el porcentaje de enfriamiento: "))


T_max = 149.9
P_max = 5.2
N_min = 15

alarma_T = Temperatura_R > T_max
alarma_P = Presion_R >= P_max
alarma_N = Nivel_T < N_min

print(f"Estado final de la alarma {alarma_T == alarma_T}")
print(f"Estado final de la alarma {alarma_N}")
print(f"Estado final de la alarma {Presion_R == 0.0}")

