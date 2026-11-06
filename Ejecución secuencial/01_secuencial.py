import time

def realizar_ejercicio(grupo_muscular, ejercicio, series, segundos_por_serie):
    print(f"\n--- Iniciando bloque de {grupo_muscular}: {ejercicio} ---")
    for serie in range(1, series + 1):
        print(f"  [{grupo_muscular}] Ejecutando serie {serie}/{series} de {ejercicio}...")
        time.sleep(segundos_por_serie)  # Simula el tiempo de ejecución y descanso
    print(f"Completado: {ejercicio} ({grupo_muscular}) finalizado.")

if __name__ == "__main__":
    print("PLAN DE ENTRENAMIENTO SECUENCIAL (DÍA DE EMPUJE: PECHO, HOMBROS Y TRÍCEPS)")
    inicio = time.perf_counter()

    # Ejecución secuencial: no se pasa al siguiente músculo hasta terminar el actual
    realizar_ejercicio("Pecho", "Press de banca", series=3, segundos_por_serie=1)
    realizar_ejercicio("Hombros", "Press militar con mancuernas", series=3, segundos_por_serie=1)
    realizar_ejercicio("Tríceps", "Extensión en polea alta", series=3, segundos_por_serie=1)

    fin = time.perf_counter()
    print(f"\nEntrenamiento del día completado en: {fin - inicio:.2f} segundos.")
