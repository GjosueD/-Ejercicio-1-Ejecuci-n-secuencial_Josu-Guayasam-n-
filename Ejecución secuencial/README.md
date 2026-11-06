# Ejercicio 1: Ejecución Secuencial

## Descripción del Ejemplo (Vida Diaria)
Este script de Python simula un **plan de entrenamiento de un día en el gimnasio enfocado en Pecho, Hombros y Tríceps**. 

En una **ejecución secuencial**, cada tarea se realiza una tras otra en un orden estricto:
1. Primero se completan todas las series de **Pecho** (*Press de banca*).
2. Una vez terminado pecho, se pasa a **Hombros** (*Press militar con mancuernas*).
3. Finalmente, al terminar hombros, se realiza **Tríceps** (*Extensión en polea alta*).

Ningún ejercicio inicia hasta que el anterior haya finalizado por completo, por lo que el tiempo total de ejecución es la suma de cada bloque de entrenamiento.

## Estructura del Proyecto
- `01_secuencial.py`: Script de Python que simula la rutina secuencial.
- `docker-compose.yml`: Configuración del contenedor con Python para ejecutar el script.
- `README.md`: Instrucciones de uso.

## Cómo ejecutar el script con Docker Compose

1. Abre una terminal y ubícate en la carpeta del ejercicio:
   ```bash
   cd "Ejecución secuencial"
   ```

2. Ejecuta el contenedor utilizando **Docker Compose**:
   ```bash
   docker compose up
   ```

3. Para eliminar el contenedor una vez finalizada la ejecución:
   ```bash
   docker compose down
   ```
