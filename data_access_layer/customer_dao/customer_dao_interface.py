from abc import abstractmethod, ABC

from entities.customer_class import Customer


class CustomerDAOInt(ABC):

    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_entry_by_id(self, customer_id: int) -> bool:
        pass