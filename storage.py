"""This unit contains an abstract class Storage to be inherited by other
classes saving structure"""
from abc import ABC, abstractmethod
# -------------------------------------------------------------------------


class Storage(ABC):
    """The Storage class is an abstract base class"""
    @abstractmethod
    def __init__(self, items: dict, capacity: int) -> None:
        """Initialization of the Storage class

        :param items: A dictionary with goods and amount
        :param capacity: The capacity of the storage
        """
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, item: str, amount: int) -> None:
        """This method adds an item to the storage

        :param item: The item to add
        :param amount: The amount of the item to add
        """
        self.items.setdefault(item, 0)
        self.items[item] += amount

    @abstractmethod
    def remove(self, item: str, amount: int):
        """This method removes an item from the storage

        :param item: The item to remove
        :param amount: The amount of item to remove
        """
        if self.items[item] == amount:
            del self.items[item]

        else:
            self.items[item] -= amount

    @abstractmethod
    def get_free_space(self) -> int:
        """This method returns the free space of the storage

        :return: The free space of the storage
        """
        return self._capacity - sum(self._items.values())

    @property
    @abstractmethod
    def items(self) -> dict:
        """This method returns all items placed in the storage

        :return: A dictionary with all items data
        """
        return self._items

    @abstractmethod
    def get_unique_items_count(self) -> str:
        """This method returns the string representing unique items
        placed in the storage

        :return: The string representing unique items
        """
        items_count = '\n'.join([f'{count} {item}'
                                 for item, count in self.items.items()])

        return items_count

    @abstractmethod
    def __repr__(self):
        """This method returns the representing of the Storage class

        :return: The representation of the Storage class
        """
        return f"Storage(items = {self.items}, capacity = {self._capacity}"
