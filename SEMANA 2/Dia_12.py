sustancia = {

    "nombre" : "Benceno",

    "codigo_un" : 1114,

    "inflamable" : True,

    "nivel_riesgo" : 3


}

print(f"monitoreando {sustancia['nombre']} - Nivel de riesgo inicial: {sustancia['nivel_riesgo']}")

sustancia["nivel_riesgo"] = 5
sustancia["fase emergencia"] = "Evacuacion"

print(sustancia) 