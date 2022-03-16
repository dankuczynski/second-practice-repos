from customer_exceptions.connection_problem import ConnectionProblem
from customer_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInt
from entities.customer_class import Customer
from utils.connection_module import connection


class CustomerDAOImp(CustomerDAOInt):
    def create_customer_entry(self, customer: Customer) -> Customer:
        try:
            sql = "insert into customers values(default, %s, %s) returning customer_id"
            cursor = connection.cursor()
            cursor.execute(sql, (customer.first_name, customer.last_name))
            connection.commit()
            returned_id = cursor.fetchone()[0]
            customer.customer_id = returned_id
            return customer
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))

    def delete_customer_entry_by_id(self, customer_id: int) -> bool:
        try:
            sql = "delete from customers where customer_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [customer_id])
            connection.commit()
            if cursor.rowcount != 0:
                return True
            else:
                raise NothingDeleted("No record was deleted")
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))
