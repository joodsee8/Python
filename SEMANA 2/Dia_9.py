print("Ingresa los siguientes valores, utiliza decimales")

nivel_pH = float(input("Nivel de pH:"))
temperatura = float(input("Temperatura en °C: "))

if nivel_pH <= 0.0 or nivel_pH > 14.0: 
  print("ERROR Lectura de pH fuera de rango. Detener flujo.")

elif 0.0 < nivel_pH <= 2.5:
  print("Peligro: Ácido Fuerte. Enrutando a tanque de titanio.")

elif nivel_pH > 2.5 and nivel_pH < 6.5:
    print("Aviso: Ácido Moderado. Enrutando a tanque de neutralización A.")

elif 6.5 <= nivel_pH <= 7.5:
 if temperatura > 35.0:
   print("Fluido Neutro pero Térmicamente Contaminado: Enrutando a torre de enfriamiento.")
 
 elif temperatura <= 35.0:
   print("Fluido 100% Seguro: Liberando a drenaje pluvial.")

elif nivel_pH > 7.5 and nivel_pH <= 11.5:
  print("Aviso: Alcalino Moderado. Enrutando a tanque de neutralización B.")

else:
  print("Peligro: Alcalino Fuerte. Enrutando a tanque de polímero.")
