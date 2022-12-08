"""This unit contains the Shop class representing a shop for different
items"""
from storage import Storage
# -------------------------------------------------------------------------


class Shop(Storage):
    """The Shop class provides all methods to work with shop"""
    def __init__(self, items: dict, capacity: int = 20) -> None:
        """Initialization of the Shop class

        :param items: A dictionary with goods and amount
        :param capacity: The capacity of the shop
        """

        items = items if len(items) <= 5 else items.items()[:5]
        super().__init__(items, capacity)

    def add(self, item: str, amount: int) -> bool:
        """This method adds an item to the shop

        :param item: The item to add
        :param amount: The amount of the item to add
        """

        if self.get_free_space() >= amount:

            if len(self.items) < 5:
                super().add(item, amount)
                return True

            elif item.lower() in self.items:
                super().add(item, amount)
                return True

        print('В магазине недостаточно места, попробуйте что-то другое')
        return False

    def remove(self, item: str, amount: int) -> bool:
        """This method removes an item from the shop

        :param item: The item to remove
        :param amount: The amount of item to remove
        """

        if self.items.get(item, 0) < amount:

            print(f'В магазине недостаточно товара {item} выберите другой')
            return False

        print('Нужное кол-во товара есть в магазине')
        super().remove(item, amount)
        return True

    def get_free_space(self) -> int:
        """This method returns the free space of the shop

        :return: The free space of the shop
        """

        return super().get_free_space()

    @property
    def items(self) -> dict:
        """This method returns all items placed in the shop

        :return: A dictionary with all items data
        """

        return super().items

    def get_unique_items_count(self) -> str:
        """This method returns the string representing unique items 
        placed in the shop

        :return: The string representing unique items
        """

        return super().get_unique_items_count()

    def __repr__(self) -> str:
        """This method returns the representing of the Shop class

        :return: The representation of the Shop class
        """

        return f"Shop(items = {self.items}, capacity = {self._capacity}"
