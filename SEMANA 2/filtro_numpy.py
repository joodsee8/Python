import numpy as np

temperaturas_hist = np.array([145.2, 160.5, 155.0, 182.3, 140.0, 175.8, 150.5, 190.1, 138.4])
mascara_critica = temperaturas_hist > 170.0
picos_temperatura = np.array(temperaturas_hist[mascara_critica])

print(f"Anomalias detectadas: {len(picos_temperatura)}")
print(f"Picos de temperatura: {picos_temperatura}" )