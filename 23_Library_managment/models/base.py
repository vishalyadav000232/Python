from abc import ABC , abstractmethod

class Base(ABC):
    @abstractmethod
    def save(self):
        pass