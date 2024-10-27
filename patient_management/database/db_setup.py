import psycopg2
from psycopg2 import sql
from cryptography.fernet import Fernet
import bcrypt
import logging
from ..utils.logging_config import setup_logging
from ..utils.db_config import load_db_config

# Call this early on
setup_logging()
logger = logging.getLogger(__name__)

db_config = load_db_config()
DB_NAME = db_config['db_name']
DB_HOST = db_config['host']
DB_USER = db_config['user']
DB_PASSWORD = db_config['password']

# Establish connection to PostgreSQL server, without specifying a database
def connect_to_postgres():
    """Connects to the PostgreSQL server without specifying a database."""
    try:
        return psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
        )
    except psycopg2.OperationalError as e:
        logger.error(f"Unable to connect to PostgreSQL server: {e}")
        return None

# Establish connection to the specified database
def connect_to_database(dbname):
    """Attempts to connect to the specified PostgreSQL database."""
    try:
        return psycopg2.connect(
            host=DB_HOST,
            database=dbname,
            user=DB_USER,
            password=DB_PASSWORD,
        )
    except psycopg2.OperationalError:
        return None

# Function to create the database if it doesn't exist
def create_database():
    """Creates the database if it does not exist."""
    connection = connect_to_postgres()
    if connection:
        connection.autocommit = True
        cursor = connection.cursor()

        try:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            logger.info(f"Database '{DB_NAME}' created successfully.")
        except psycopg2.errors.DuplicateDatabase:
            logger.info(f"Database '{DB_NAME}' already exists.")
        except Exception as e:
            logger.erro(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to insert default superuser
def insert_default_superuser(cursor):
    # Check if the default superuser already exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", ('admin',))
    count = cursor.fetchone()[0]

    if count == 0:
        # Hash the default password
        default_password = 'Super1!'
        password_hash = bcrypt.hashpw(default_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Insert default superuser into the database
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            ('admin', password_hash)
        )
        logger.info("Default superuser 'admin' created.")
    else:
        logger.info("Superuser 'admin' already exists.")

# Execute SQL script to set up database schema
def execute_sql_script():
    """Executes the SQL script to set up the database schema."""
    connection = connect_to_database(DB_NAME)
    if connection is None:
        logger.error(f"Could not connect to database '{DB_NAME}'.")
        return

    cursor = connection.cursor()

    try:
        with open('patient_management/database/setup.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
            cursor.execute(sql_script)  # Executes the entire script at once
        # Insert default superuser (admin)
        insert_default_superuser(cursor)
        connection.commit()
    except Exception as e:
        logger.error(f"Error executing SQL script: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
        

# Generate and load encryption key
def generate_encryption_key():
    """Generates or loads the encryption key used for secure data storage."""
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
            logger.info("Encryption key loaded.")
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
            logger.info("Encryption key generated and saved.")
    return key

# Main setup logic
def main():
    """Main function to handle database creation and schema setup."""
    # Step 1: Try to connect to the database
    if connect_to_database(DB_NAME) is None:
        logger.info(f"Database '{DB_NAME}' not found. Attempting to create it.")
        create_database()  # Create the database if it doesn't exist

    # Step 2: Ensure the database schema is set up
    execute_sql_script()

    # Step 3: Generate or load encryption key
    generate_encryption_key()

# Entry point for script execution
if __name__ == "__main__":
    main()
