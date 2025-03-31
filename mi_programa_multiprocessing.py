import multiprocessing
import numpy as np
import os
from datetime import datetime

# Definir el número de procesos según el número de CPUs disponibles
num_cpus = multiprocessing.cpu_count()

# Tamaño de los datos
data_size = 1000000  # Ajustar según el tamaño deseado

# Crear carpeta de resultados si no existe
os.makedirs("resultados", exist_ok=True)

# Generar el nombre del archivo de resultados con versión (fecha y hora)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
resultado_file = f"resultados/suma_{timestamp}.txt"

# Función para calcular la suma parcial
def suma_parcial(data_chunk):
    return np.sum(data_chunk)

# Generación de datos en el proceso principal
data = np.random.randint(0, 100, size=data_size)
print(f'Proceso principal: Datos generados con tamaño {data_size}')

# Dividir los datos en fragmentos iguales para cada proceso
chunk_size = data_size // num_cpus
data_chunks = [data[i:i + chunk_size] for i in range(0, data_size, chunk_size)]

# Crear un pool de procesos
with multiprocessing.Pool(processes=num_cpus) as pool:
    # Calcular la suma de cada fragmento en paralelo
    sumas_parciales = pool.map(suma_parcial, data_chunks)

# Calcular la suma total sumando los resultados parciales
total_sum = sum(sumas_parciales)

# Guardar el resultado en un archivo de la carpeta resultados
with open(resultado_file, "w") as file:
    file.write(f"Suma total = {total_sum}\n")
    print(f"Resultado guardado en {resultado_file}")
