project_name = 'Todo List'
print('#' * 30)
print('        ', project_name)
print('#' * 30)


def all_options():
    dicts = {
        1: 'add a task',
        2: 'edit a task',
        3: 'display task list',
        4: 'delete a task',
        5: 'delete all task',
        0: 'exit'
    }
    for k, v in dicts.items():
        print('press', k, '-----', v)


task_list = []
all_options()
while True:
    option = int(input('Choose an option from the above : '))
    if option == 1:
        task = input('Enter your task which you want to add ')
        task_list.append(task)
    elif option == 2:
        print('Tasks list :', task_list)
        pos = int(input('Enter the position on which you want to edit '))
        task = input('Enter a task which you want to add ')
        task_list[pos] = task
    elif option == 3:
        if len(task_list) > 0:
            print('All tasks are :')
            for task in task_list:
                print(task)
        else:
            print('There is no task in my list')
    elif option == 4:
        print('Tasks list :', task_list)
        pos = int(input('Enter the position which you want delete '))
        del task_list[pos]
    elif option == 5:
        task_list.clear()
        print('All tasks are removed')
    elif option == 0:
        break
    else:
        all_options()

