from customer_exceptions.bad_id import BadId
from customer_exceptions.bad_name import BadName
from data_access_layer.customer_dao.customer_dao import CustomerDAOImp
from entities.customer_class import Customer
from service_layer.customer_service.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


# create method validation tests

def test_catch_no_string_first_name():
    try:
        customer_service.service_create_customer_record(Customer(0, 31267, "this is fine"))
        assert False
    except BadName as e:
        assert str(e) == "Please enter a valid first name"


def test_catch_no_string_last_name():
    try:
        customer_service.service_create_customer_record(Customer(0, "this is fine", 32783627))
        assert False
    except BadName as e:
        assert str(e) == "Please enter a valid last name"


def test_catch_first_name_too_long():
    try:
        customer_service.service_create_customer_record(Customer(0, "This name is way too long", "thi is fine"))
        assert False
    except BadName as e:
        assert str(e) == "First name is too long: it should be no more than 20 characters"


def test_catch_last_name_too_long():
    try:
        customer_service.service_create_customer_record(Customer(0, "This is fine", "This name is way too long"))
        assert False
    except BadName as e:
        assert str(e) == "Last name is too long: it should be no more than 20 characters"


def test_catch_non_int_typecastable_value():
    try:
        customer_service.service_delete_customer_record_by_id("one")
    except BadId as e:
        assert str(e) == "Please provide a valid customer ID"
