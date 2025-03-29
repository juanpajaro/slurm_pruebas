#!/bin/bash
#SBATCH --job-name=mi_tarea_paralela       # Nombre del trabajo
#SBATCH --output=resultados/salida_%j.out  # Archivo de salida en la carpeta resultados
#SBATCH --error=resultados/error_%j.err    # Archivo de errores en la carpeta resultados
#SBATCH --nodes=4                          # Número de nodos solicitados
#SBATCH --ntasks=1                         # Número total de tareas (una sola tarea en varios nodos)
#SBATCH --ntasks-per-node=1                 # Una tarea por nodo
#SBATCH --cpus-per-task=16                 # Número de núcleos por tarea
#SBATCH --time=01:00:00                    # Tiempo máximo de ejecución
#SBATCH --partition=general                # Partición a utilizar

# Cargar el entorno Conda
source /zine/apps/anaconda_salud/etc/profile.d/conda.sh
conda activate mpi_env

# Crear carpeta de resultados si no existe
mkdir -p resultados

# Cargar el entorno MPI
module load mpi

# Ejecutar la tarea con srun
srun --mpi=pmix python mi_programa_mpi.py
