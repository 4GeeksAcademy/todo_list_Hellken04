import csv

tasks=[]

def add_one_task (title):
    task.append (title)

def print_list ():
    i=0
    for elemento in tasks:
        print (str(i) + elemento)
        i=i+1
def delete_task (number_to_delete):
    tasks.pop(number_to_delete)

def save_todos ():
    i=0
    with open("todos.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    for todo in tasks: 
        fila = [i,todo]
        escritor.writerows(fila)
        i=i+1


