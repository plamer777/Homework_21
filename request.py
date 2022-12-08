"""This unit contains the Request class representing a user's request to
send an item from store to shop and vice versa"""


class Request:
    """The Request class representing a user's request to send an item"""
    def __init__(self, task: str) -> None:
        """This constructor of the Request class

        :param task: a string with current task
        """
        task = task.split(' ')

        self._from = task[4]
        self._to = task[6]
        self._amount = int(task[1])
        self._product = task[2]

    @property
    def from_(self) -> str:
        """This method returns the start point to send item from

        :return a string representing the start point
        """
        return self._from

    @property
    def to(self) -> str:
        """This method returns the end point to deliver item to

        :return a string representing the end point
        """

        return self._to

    @property
    def amount(self) -> int:
        """This method returns the amount of items to send

        :return an integer representing the amount of items
        """

        return self._amount

    @property
    def product(self) -> str:
        """This method returns the name of item

        :return a string representing the name of item
        """

        return self._product

    def __repr__(self) -> str:
        """This method returns the representing of the Request class

        :return: The representation of the Request class
        """

        return f'Request({self._from}, {self._to}, {self._amount}, ' \
               f'{self._product})'
