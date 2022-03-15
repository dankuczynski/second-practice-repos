from customer_exceptions.bad_id import BadId
from customer_exceptions.bad_name import BadName
from entities.customer_class import Customer
from service_layer.customer_service.customer_service_interface import CustomerServiceInt


class CustomerServiceImp(CustomerServiceInt):
    def service_create_customer_record(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise BadName("Please enter valid first name")
        if type(customer.last_name) != str:
            raise BadName("Please enter valid last name")
        if len(customer.first_name) > 20:
            raise BadName("First name is too long: it should be no more that 20 characters")
        if len(customer.last_name) > 20:
            raise BadName("Last name is too long: it should be no more than 20 characters")
        return self.customer_dao.create_customer_entry(customer)

    def service_delete_customer_record_by_id(self, customer_id: str) -> bool:
        try:
            return self.customer_dao.delete_customer_entry_by_id(int(customer_id))
        except ValueError:
            raise BadId("Please provide a valid customer ID")
