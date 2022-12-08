"""This unit contains all necessary functions to simulate delivery process"""
from time import sleep
from request import Request
from storage import Storage
from store import Store
from shop import Shop
from source import STORE_ITEMS, SHOP_ITEMS
# -------------------------------------------------------------------------


def main() -> None:
    """The main function to manage the delivery process"""
    while True:
        # creating a task, start and end points
        task = create_new_task()
        start_point, end_point = define_start_and_end_points(task)

        if not start_point.remove(task.product, task.amount):
            continue

        elif not end_point.add(task.product, task.amount):
            start_point.add(task.product, task.amount)
            continue

        # execution of the requested task
        execute_task(task, start_point, end_point)

        user_answer = input("\nХотите перевезти еще товар? (Y/N): ").lower()
        if user_answer != "y":
            break


def execute_task(task: Request, start_point: Storage, end_point: Storage) \
        -> None:
    """This function executes the specified task

    :param task: the task to execute
    :param start_point: the start point to send item from
    :param end_point: the end point to deliver item to
    """
    print(f'Курьер забрал {task.amount} {task.product} из {task.from_}')
    sleep(1)
    print(f'Курьер везет {task.amount} {task.product} из {task.from_}')
    sleep(1)
    print(f'Курьер доставил {task.amount} {task.product} в {task.to}')

    print('\nОбновляем ассортимент, пожалуйста подождите')
    for i in range(10):
        print('.', end='')
        sleep(0.5)

    print(f"\nВ {task.from_} хранится:\n"
          f"{start_point.get_unique_items_count()}")
    print(f"\nВ {task.to} хранится:\n"
          f"{end_point.get_unique_items_count()}")


def define_start_and_end_points(task: Request) -> tuple:
    """This function defines the start and end points

    :param task: the current task to execute

    :return: the start and end points
    """
    shop, store = create_shop_and_store()
    directions = {
        'склад': store,
        'магазин': shop
    }

    # creation of start and end points depending on the task fields
    start_point = directions.get(task.from_)
    end_point = directions.get(task.to)

    return start_point, end_point


def create_new_task() -> Request:
    """This function creates a new task

    :return: an instance of the Request class
    """
    print('Введите задачу по перевозке товара')
    task = input().lower().strip()

    user_req = Request(task)

    return user_req


def create_shop_and_store() -> tuple:
    """This function creates an instances of the Store and Shop classes

    :return: an instances of the Store and Shop classes
    """
    store = Store(STORE_ITEMS)
    shop = Shop(SHOP_ITEMS)

    return shop, store
