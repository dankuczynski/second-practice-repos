from psycopg import connect, OperationalError
import os

from customer_exceptions.connection_problem import ConnectionProblem


def create_connection():
    try:
        connection_object = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DB"),
            user=os.environ.get("USERNAME"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT"),
        )
        return connection_object
    except OperationalError as e:
        print(str(e))


connection = create_connection()

print(connection)
