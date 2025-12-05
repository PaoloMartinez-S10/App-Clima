import json
import os

# --- CONFIGURACIÓN ---
ARCHIVO_DATOS = "registro_clima.json"

# --- 1. PERSISTENCIA DE DATOS (Guardar y Cargar) ---

def cargar_datos():
    """Carga los datos del JSON. Si no existe, devuelve una lista vacía."""
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return []
    return []

def guardar_datos(datos):
    """Guarda la lista completa en el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("Datos guardados automáticamente.")
    except Exception as e:
        print(f" Error al guardar datos: {e}")

# --- 2. FUNCIONES PRINCIPALES ---

def registrar_ciudad(datos):
    """Pide datos al usuario y valida que los números sean correctos."""
    print("\n--- 📝 Registrar Nueva Ciudad ---")
    ciudad = input("Nombre de la ciudad: ").strip().title()
    pais = input("País: ").strip().title()
    
    # Validación de números (Bucle infinito hasta que el usuario ponga un número)
    while True:
        try:
            temp_min = float(input("Temperatura Mínima (°C): "))
            temp_media = float(input("Temperatura Media (°C): "))
            break
        except ValueError:
            print(" Error: Por favor ingresa un número válido (usa punto para decimales).")

    nuevo_registro = {
        "ciudad": ciudad,
        "pais": pais,
        "minima": temp_min,
        "media": temp_media
    }
    
    datos.append(nuevo_registro)
    guardar_datos(datos) # Guardamos inmediatamente
    print(f" ¡{ciudad} registrada con éxito!")

def ver_registros(datos):
    """Imprime una tabla limpia con todos los datos."""
    if not datos:
        print("\n La base de datos está vacía.")
        return

    print("\n" + "="*65)
    print(f"{'CIUDAD':<20} | {'PAÍS':<15} | {'MÍN (°C)':<10} | {'MEDIA (°C)':<10}")
    print("-" * 65)

    for d in datos:
        print(f"{d['ciudad']:<20} | {d['pais']:<15} | {d['minima']:<10} | {d['media']:<10}")
    print("="*65)

# --- 3. FUNCIONES DE BÚSQUEDA Y ANÁLISIS ---

def buscar_ciudad(datos):
    """Filtra y muestra ciudades que coincidan con la búsqueda."""
    if not datos:
        print("\n No hay datos para buscar.")
        return

    busqueda = input("\n Escribe la ciudad o país a buscar: ").strip().lower()
    
    # List comprehension para filtrar
    resultados = [d for d in datos if busqueda in d['ciudad'].lower() or busqueda in d['pais'].lower()]

    if resultados:
        print(f"\n Se encontraron {len(resultados)} coincidencia(s):\n")

        # Reutilizamos la lógica de impresión de la tabla
        print(f"{'CIUDAD':<20} | {'PAÍS':<15} | {'MÍN (°C)':<10} | {'MEDIA (°C)':<10}")
        print("-" * 65)
        for d in resultados:
            print(f"{d['ciudad']:<20} | {d['pais']:<15} | {d['minima']:<10} | {d['media']:<10}")
    else:
        print(f"No se encontraron resultados para '{busqueda}'.")

def mostrar_estadisticas(datos):
    """Calcula máximos, mínimos y promedios."""
    if not datos:
        print("\n Necesitas registrar datos antes de ver estadísticas.")
        return
    print("\n" + "="*65)

    # Lógica de análisis
    ciudad_mas_caliente = max(datos, key=lambda x: x['media'])
    ciudad_mas_fria = min(datos, key=lambda x: x['minima'])
    
    suma_medias = sum(d['media'] for d in datos)
    promedio_global = suma_medias / len(datos)

    print("\n--- REPORTE CLIMÁTICO --- ")
    print(f"\n Ciudad más calurosa (Media): {ciudad_mas_caliente['ciudad']} ({ciudad_mas_caliente['media']}°C)\n")
    print(f"\n Ciudad más fría (Mínima):    {ciudad_mas_fria['ciudad']} ({ciudad_mas_fria['minima']}°C)\n")
    print(f"\n Temperatura Media Global:     {promedio_global:.2f}°C\n")
    print(f"\n Total de ciudades registradas: {len(datos)}\n")
    print("-------------------------------")

# --- 4. MENÚ PRINCIPAL ---

def main():
    datos = cargar_datos()

    while True:
        print("\n" + "="*65)
        print("\n GESTOR DE CLIMA MUNDIAL")
        print("1. Registrar nueva ciudad")
        print("2. Ver listado completo")
        print("3. Buscar ciudad o país")
        print("4. Ver Estadísticas y Análisis")
        print("5. Salir")
        
        opcion = input("\n👉 Elige una opción: ")
        
        if opcion == "1":
            registrar_ciudad(datos)
        elif opcion == "2":
            ver_registros(datos)
        elif opcion == "3":
            buscar_ciudad(datos)
        elif opcion == "4":
            mostrar_estadisticas(datos)
        elif opcion == "5":
            print("¡Gracias por usar el gestor! Tus datos están guardados.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
