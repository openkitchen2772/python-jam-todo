EXIT_CMD = 'exit'

todo_list = [
    # { name: '', completed: False, interval: 'weekly' }
]

def print_help():
    print(f"""
Help: use number or command name below to perform intended action.
[type 'help' to show this help message again]
(1) print - print current to-do list.
(2) add - add new task to the list.
(3) remove - remove task from the list by name or number.
(4) complete - complete a task by its name or index.
(5) interval - set the interval of task by its name or index.
(6) {EXIT_CMD} - exit the program.
    """)

def get_interval_name(interval):
    if interval == 0:
        return 'None'
    elif interval == 1:
        return 'Daily'
    elif interval == 2:
        return 'Weekly'
    elif interval == 3:
        return 'Monthly'
    else:
        return 'Unknown'

def get_task_idx_by_name_or_number(value):
    if value.isnumeric():
        if int(value) - 1 < len(todo_list):
            return int(value) - 1
    else:
        for i in range(len(todo_list)):
            tn = todo_list[i]['name']
            if tn == value:
                return i
    # not found in either way
    return -1

def print_list():
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task['name']} - completed: {task['completed']}, interval: {task['interval']}")

def add_task():
    task_name = input('Name the task to add: ')
    if task_name == '':
        print('Please enter name for the to-do task.')
        return
    else:
        todo_list.append({'name': task_name, 'completed': False, 'interval': 'None'})
        print(f'Added task - {task_name}.')

def remove_task():
    task = input('Task name or number to remove: ')
    deleted_task_name = ''
    # remove task using number or task name
    task_index = get_task_idx_by_name_or_number(task)
    if task_index > -1:
        deleted_task_name = todo_list[task_index]['name']
        todo_list.pop(task_index)
    # after removal
    if deleted_task_name == '':
        print('Task not found in list.')
    else:
        print(f'Removed task - {deleted_task_name}.')

def complete_task():
    task = input('Task name or number to complete: ')
    completed_task_name = ''
    task_index = get_task_idx_by_name_or_number(task)
    if task_index > -1:
        completed_task_name = todo_list[task_index]['name']
        todo_list[task_index]['completed'] = True
    # after completion
    if completed_task_name == '':
        print('Task not found in list.')
    else:
        print(f'Completed task - {completed_task_name}.')

def set_task_interval():
    updated_task = ''
    updated_interval = ''
    task = input('Task name or number to set interval: ')
    task_index = get_task_idx_by_name_or_number(task)
    if task_index > -1:
        updated_task = todo_list[task_index]['name']
        interval = input('Please enter interval (0 - None, 1 - daily, 2 - weekly, 3 - monthly): ')
        if interval.isnumeric():
            updated_interval = get_interval_name(int(interval))
            todo_list[task_index]['interval'] = get_interval_name(int(interval))
    if updated_task == '':
        print('Task not found in list.')
    elif updated_interval == -1:
        print('Please enter an interval from the options.')
    else:
        print(f'Set interval - {updated_task} *{updated_interval}*.')

def process_cmd(cmd):
    if cmd == 'help' or cmd == '?' or cmd == 'h':
        print_help()
    elif cmd == 'print' or cmd == '1':
        print_list()
    elif cmd == 'add' or cmd == '2':
        add_task()
    elif cmd == 'remove' or cmd == '3':
        remove_task()
    elif cmd == 'complete' or cmd == '4':
        complete_task()
    elif cmd == 'interval' or cmd == '5':
        set_task_interval()
    elif cmd == EXIT_CMD:
        print('Goodbye!')
    else:
        print_help()

if __name__ == '__main__':
    print('Welcome to To-Do list program, please refer to help for guide.')
    print_help()
    command = ''
    while command != EXIT_CMD:
        command = input('Command: ')
        process_cmd(command)
