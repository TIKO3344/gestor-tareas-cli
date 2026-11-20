tareas = []

def agregar_tarea(titulo):
    tareas.append({"titulo": titulo, "completada": False})
    print(f"Tarea '{titulo}' agregada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    for i, t in enumerate(tareas, 1):
        estado = "[X]" if t["completada"] else "[ ]"
        print(f"{i}. {estado} {t['titulo']}")

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS CLI (AYUDA) ===")
    print("Seleccione una opción del 1 al 5:")
    print("1. Agregar una nueva tarea")
    print("2. Listar todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar una tarea existente")
    print("5. Salir del programa")

if __name__ == "__main__":
    mostrar_menu()
