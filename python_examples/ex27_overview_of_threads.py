import threading


def some_task(task_name, limit=10, delay=0.25):
    ct1 = threading.current_thread()
    for i in range(limit):
        print(f'executing the task {task_name}, loop count = {i} using the thread {ct1.name}')


if __name__ == '__main__':
    ct = threading.current_thread()
    print(f'start of the script execution using the thread {ct.name}')
    # some_task('task-1')
    # some_task('task-2')
    # some_task('task-3')
    t1 = threading.Thread(name='t1', target=some_task, args=('task-1', ))
    t2 = threading.Thread(name='t2', target=some_task, args=('task-2', 15))
    t3 = threading.Thread(name='t3', target=some_task, args=('task-1', 15))
    t1.start()
    t2.start()
    t3.start()
    print(f'end of the script execution using the thread {ct.name}')
