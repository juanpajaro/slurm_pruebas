from mpi4py import MPI
import numpy as np
import os
from datetime import datetime

# Inicialización del entorno MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Definición del tamaño de los datos
data_size = 10000

# Crear carpeta de resultados si no existe
if rank == 0:
    os.makedirs("resultados", exist_ok=True)

# Generar el nombre del archivo de resultados con versión (fecha y hora)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
resultado_file = f"resultados/suma_{timestamp}.txt"

# Generación de datos en el nodo principal
if rank == 0:
    data = np.random.randint(0, 100, size=data_size)
    print(f'Nodo {rank}: Datos generados')
else:
    data = None

# Preparación del contenedor de datos en cada nodo
data_chunk = np.empty(data_size // size, dtype=int)

# Distribuir los datos (scatter)
comm.Scatter(data, data_chunk, root=0)

# Calcular la suma local en cada nodo
local_sum = np.sum(data_chunk)
print(f'Nodo {rank}: Suma local = {local_sum}')

# Reducción de las sumas locales en el nodo principal
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# Guardar el resultado en un archivo de la carpeta resultados
if rank == 0:
    with open(resultado_file, "w") as file:
        file.write(f"Suma total = {total_sum}\n")
        print(f"Resultado guardado en {resultado_file}")
