"""This unit contains the Store class representing a store for different
items"""
from storage import Storage
# -------------------------------------------------------------------------


class Store(Storage):
    """The Store class provides all methods to work with store"""
    def __init__(self, items: dict, capacity: int = 100) -> None:
        """Initialization of the Store class

        :param items: A dictionary with goods and amount
        :param capacity: The capacity of the store
        """

        super().__init__(items, capacity)

    def add(self, item: str, amount: int) -> bool:
        """This method adds an item to the store

        :param item: The item to add
        :param amount: The amount of the item to add
        """

        if amount <= 0:
            print('Укажите кол-во товара больше 0')
            return False

        elif self.get_free_space() < amount:
            amount = self.get_free_space()
            print(f'На складе не хватает места, осталась {amount} свободных '
                  f'мест, попробуйте подождать или разместить меньше товара')
            return False

        super().add(item, amount)
        return True

    def remove(self, item: str, amount: int) -> bool:
        """This method removes an item from the store

        :param item: The item to remove
        :param amount: The amount of item to remove
        """

        if amount <= 0:
            print('Укажите кол-во товара больше 0')
            return False

        elif self.items.get(item, 0) < amount:

            print(f'На складе {self.items.get(item, 0)} ед. товара {item} '
                  f'выберите что-то еще или попробуйте заказать меньше')
            return False

        print('Нужное кол-во товара есть на складе')
        super().remove(item, amount)
        return True

    def get_free_space(self) -> int:
        """This method returns the free space of the store

        :return: The free space of the store
        """

        return super().get_free_space()

    @property
    def items(self) -> dict:
        """This method returns all items placed in the store

        :return: A dictionary with all items data
        """

        return super().items

    def get_unique_items_count(self) -> str:
        """This method returns the string representing unique items 
        placed in the store

        :return: The string representing unique items
        """

        return super().get_unique_items_count()

    def __repr__(self) -> str:
        """This method returns the representing of the Store class

        :return: The representation of the Store class
        """

        return f"Store(items = {self.items}, capacity = {self._capacity}"
