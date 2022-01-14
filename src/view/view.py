from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def show_result(self, result):
        pass
