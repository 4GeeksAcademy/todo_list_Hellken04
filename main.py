import csv
import argparse
import os

tasks = []

def load_todos():
    
    global tasks
    if os.path.exists("todos.csv"):
        with open("todos.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            tasks = [fila[1] for fila in lector if len(fila) > 1]

def add_one_task(title):
    tasks.append(title)
    save_todos()
    print(f"Tarea añadida: '{title}'")

def print_list():
    if not tasks:
        print("No hay tareas pendientes.")
        return
    for i, elemento in enumerate(tasks):
        print(f"{i}: {elemento}")

def delete_task(number_to_delete):
    eliminada = tasks.pop(number_to_delete)
    save_todos()
    print(f"Tarea eliminada: '{eliminada}'")
    

def save_todos():
    with open("todos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for i, todo in enumerate(tasks): 
            escritor.writerow([i, todo])

def main():
    load_todos()

    parser = argparse.ArgumentParser(description="A To Do Tool")
    
    # Creamos el contenedor para los subcomandos (add, list, delete)
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponibles")

    # Subcomando: add
    parser_add = subparsers.add_parser("add", help="Añadir una nueva tarea")
    parser_add.add_argument("titulo", type=str, help="Título o descripción de la tarea")

    # Subcomando: list
    subparsers.add_parser("list", help="Listar todas las tareas")

    # Subcomando: delete
    parser_del = subparsers.add_parser("delete", help="Eliminar una tarea por su número")
    parser_del.add_argument("numero", type=int, help="Número de la tarea a eliminar")

    # Subcomando: save
    parser_del = subparsers.add_parser("save", help="Guardar las tareas en memoria en el cvs")
    
    # Parsear los argumentos de la terminal
    args = parser.parse_args()

    # Evaluar qué subcomando escribió el usuario
    if args.comando == "add":
        add_one_task(args.titulo)
    elif args.comando == "list":
        print_list()
    elif args.comando == "delete":
        delete_task(args.numero)
    elif args.comando == "save":
        save_todos()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
