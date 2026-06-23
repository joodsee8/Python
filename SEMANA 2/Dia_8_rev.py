# REVANCHA DIA 8

pureza = float(input("Ingresa el porcentaje de pureza de la sustancia: "))
humedad = float(input("ingresa el porcentaje de agua residual: "))
viscosidad = float(input("Ingresa la viscosidad medida en cP: "))
temp_max = float(input("ingresa la Temperatura maxima que alcanzo el reactor durante la sintesis: "))

lote_aprobado = (((pureza >= 98.5 and humedad == 0.0 and viscosidad >= 200 or viscosidad <= 300) or (pureza >= 99.8 and humedad == 0.0)) and (temp_max < 180)) 
 
print(f"Estado final: {lote_aprobado}")