from abc import ABC, abstractmethod

class View(ABC):

    @abstractmethod
    def display(self, data):
        pass


class ConsoleView(View):

    def display(self, data):
        for item in data:
            print(item)
