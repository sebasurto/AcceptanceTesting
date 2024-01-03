# Lista para almacenar las tareas
to_do_list = []
#Función para eliminar una tarea
def delete_task(task_name):
    for task in to_do_list:
        if task['name'] == task_name:
            to_do_list.remove(task)
            print(f'Task "{task_name}" has been deleted.')
            return
    print(f'Task "{task_name}" not found in the to-do list.')
#función para editar una tarea 
def edit_task(task_name, new_name, new_description, new_status):
    for task in to_do_list:
        if task['name'] == task_name:
            task['name'] = new_name
            task['description'] = new_description
            task['status'] = new_status
            print(f'Task "{task_name}" has been edited.')
            return
    print(f'Task "{task_name}" not found in the to-do list.')

# Función para agregar una nueva tarea
def add_task(name, description, status="Incomplete"):
    task = {
        'name': name,
        'description': description,
        'status': status
    }
    to_do_list.append(task)
    print(f'Task "{name}" has been added to the to-do list.')

# Función para listar todas las tareas
def list_tasks():
    if not to_do_list:
        print('The to-do list is empty.')
    else:
        print('To-Do List:')
        for idx, task in enumerate(to_do_list, start=1):
            print(f'{idx}. Name: {task["name"]}, Description: {task["description"]}, Status: {task["status"]}')

# Función para marcar una tarea como completada
def mark_task_complete(task_name):
    for task in to_do_list:
        if task['name'] == task_name:
            task['status'] = 'Complete'
            print(f'Task "{task_name}" has been marked as complete.')
            return
    print(f'Task "{task_name}" not found in the to-do list.')

# Función para borrar toda la lista de tareas
def clear_all_tasks():
    to_do_list.clear()
    print('All tasks have been cleared from the to-do list.')

# Función principal para el manejo de comandos del usuario
def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Clear All Tasks")
        print("5. Delete Task")
        print("6. Edit Task")
        print("7. Quit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            add_task(name, description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_name = input("Enter task name to mark as complete: ")
            mark_task_complete(task_name)
        elif choice == '4':
            clear_all_tasks()
        elif choice == '5':
            task_name = input("Enter task name to delete: ")
            delete_task(task_name)
        elif choice == '6':
            task_name = input("Enter task name to edit: ")
            new_name = input("Enter new task name: ")
            new_description = input("Enter new task description: ")
            new_status = input("Enter new task status: ")
            edit_task(task_name, new_name, new_description, new_status)  
        elif choice == '7':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
