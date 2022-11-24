from celery import Celery, Task, current_task
import time, os

CELERY_BROKER_URL  = os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0')#redis://127.0.0.1:6379/1
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/1')#redis://127.0.0.1:6379/0

celery_app = Celery('task', backend=CELERY_RESULT_BACKEND, broker=CELERY_BROKER_URL)


@celery_app.task()
def add(x, y):
    for status in range(10):
        print(f'|{">" * status}{" " * (10 - status)}|', end="")
        time.sleep(0.5)
    return {'x + y =': x + y}


class ClassNvsConfig(Task):
    def run(self, x, y):
        for status in range(10):
            print(f'|{">" * status}{" " * (10 - status)}|', end="")
            time.sleep(0.5)
        return {'x - y =': x - y}


ClassNvs = celery_app.register_task(ClassNvsConfig())  # ClassNvs
