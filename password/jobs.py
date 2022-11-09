from threading import Timer

import schedule

from .services import delete_expired_passes


def excluder_task():
    print('Deleting expired passes')
    delete_expired_passes()

def init_tasks():
    schedule.every(10).seconds.do(excluder_task).run()