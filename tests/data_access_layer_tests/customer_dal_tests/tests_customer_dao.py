from unittest.mock import patch

from customer_exceptions.connection_problem import ConnectionProblem
from customer_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_dao.customer_dao import CustomerDAOImp
from entities.customer_class import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_entry_success():
    # create customer object to enter into database
    customer = Customer(0, "Tom", "Jerry")
    # pass object into create method
    result_customer = customer_dao.create_customer_entry(customer)
    # check that it has a new id
    return result_customer.customer_id != 0


def test_delete_customer_entry_success():
    # pass in id of entry to be deleted into delete method
    # remember to make sure customer you are deleting i actually in the database
    result = customer_dao.delete_customer_entry_by_id(-1)
    # check boolean result of delete method
    assert result


@patch("utils.connection_module.create_customer")
def test_create_customer_operation_error_caught(mock):
    # try to run create method, have exception raised instead
    try:
        mock.side_effect = ConnectionProblem("Could not connect to database")
        customer_dao.create_customer_entry(Customer(0, "Should not", "be added"))
        assert False
    # check that our method catches and raises a new exception and has proper message
    except ConnectionProblem as e:
        assert str(e) == "Could not connect to the database"


@patch("utils.connection_module.connect.cursor")
def test_delete_customer_operation_error_caught(mock):
    # try to run delete method, have exception raised instead
    try:
        mock.side_effect = ConnectionProblem("Could not connect to the database")
        customer_dao.delete_customer_entry_by_id(0)
        assert False
    # check that our method catches and raises a new exception and has the proper message
    except ConnectionProblem as e:
        assert str(e) == "Could not connect to the database"


def test_delete_customer_no_records_changed():
    try:
        customer_dao.delete_customer_entry_by_id(1000)
        assert False
    except NothingDeleted as e:
        assert str(e) == "No record was deleted"
