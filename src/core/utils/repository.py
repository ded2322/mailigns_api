from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def show_table(self):
        pass

    @abstractmethod
    def found_one_or_none(self, **kwargs):
        pass

    @abstractmethod
    def insert_data(self, **kwargs):
        pass

    @abstractmethod
    def delete_data(self, **kwargs):
        pass
