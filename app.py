tareas = []

def completar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Índice no válido.")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        eliminada = tareas.pop(indice)
        print(f"Tarea '{eliminada['titulo']}' eliminada.")
    else:
        print("Índice no válido.")

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

if __name__ == "__main__":
    mostrar_menu()
