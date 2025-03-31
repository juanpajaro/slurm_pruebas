#!/bin/bash
#SBATCH --job-name=mi_tarea_paralela       # Nombre del trabajo
#SBATCH --output=resultados/salida_%j.out  # Archivo de salida en la carpeta resultados
#SBATCH --error=resultados/error_%j.err    # Archivo de errores en la carpeta resultados
#SBATCH --nodes=1                          # Usar un solo nodo (worker)
#SBATCH --ntasks=1                         # Una sola tarea
#SBATCH --cpus-per-task=16                 # Número de núcleos a usar (ajustar según el nodo)
#SBATCH --time=01:00:00                    # Tiempo máximo de ejecución
#SBATCH --partition=general                # Partición a utilizar

# Cargar el entorno Conda
source ~/miniconda3/etc/profile.d/conda.sh
conda activate mpi_env

# Crear carpeta de resultados si no existe
mkdir -p resultados

# Ejecutar la tarea con srun
srun --mpi=pmix python /zine/data/salud/slurm_pruebas/mi_programa_multiprocessing.py
