# Gestor de Tareas CLI

Aplicación de consola en Python para administrar tareas diarias (crear, listar, completar y eliminar).

## Requisitos Previos
- Python 3.8 o superior
- Git

## Instrucciones de Uso
1. Clona este repositorio.
2. Ejecuta el programa desde la terminal:
   ```bash
   python app.py

**5. Crea el archivo base `app.py`:**
```bash
cat << 'EOF' > app.py
tareas = []

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

if __name__ == "__main__":
    mostrar_menu()
