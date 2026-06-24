while True:
    try:
        presion_absoluta = float(input("Ingresa la presión absoluta del reactor: "))

        if presion_absoluta < 0:
            print("Advertencia Física: La presión absoluta no puede ser negativa. Intenta de nuevo.")

        elif presion_absoluta >= 0:
            print("Lectura aceptada y guardada en el sistema.")
           
            break
        
    except ValueError: 
        print("ERROR DE CAPA 8: Has ingresado texto en lugar de números. Usa únicamente dígitos.")
          