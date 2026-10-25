import time
def task(name,seconds):
    print(f'{name} started')
    time.sleep(seconds)
    print(f'{name} completed')
task('Task1',3)
task('Task2',2)
task('Task3',1)