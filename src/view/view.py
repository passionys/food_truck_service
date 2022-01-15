from abc import ABC, abstractmethod


class View(ABC):
    """
    View : abstract View class from which subclass views inherit
    """
    @abstractmethod
    def show_result(self, result):
        pass
