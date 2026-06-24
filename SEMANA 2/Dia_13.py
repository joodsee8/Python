import math

def calcular_pH(concentracion_H):
    nivel_pH = - math.log10(concentracion_H)
    return nivel_pH

def volumen_esferico(radio):
    numero_pi = math.pi
    radio3 = math.pow(radio, 3)
    Volumen_tanque = ((4/3) * numero_pi * radio3)
    return Volumen_tanque

print(
    f"El nivel de pH es {calcular_pH(0.00005)}",
    f"El volumen del tanque es: {volumen_esferico(10.5)}",
    sep = '\n'
    )


