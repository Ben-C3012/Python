import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD"),
        host=os.getenv("PGHOST"),
        database=os.getenv("PGDATABASE")
    )

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected ✅ to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


# export cursor and connection to be used in other files
def get_cursor():
    return cursor