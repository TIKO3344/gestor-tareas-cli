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
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

if __name__ == "__main__":
    mostrar_menu()
