import bcrypt
from ..database.db_setup import connect_to_database  # Import the connection function
from .db_config import load_db_config

def authenticate_user(username, password):
    db_config = load_db_config()
    DB_NAME = db_config['db_name']
    # Use the connect_to_database function to connect to the PostgreSQL database
    connection = connect_to_database(DB_NAME)
    
    if connection is None:
        print("Database connection failed.")
        return False
    
    cursor = connection.cursor()
    
    try:
        # Query to fetch the hashed password for the given username
        cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
    except Exception as e:
        print(f"Error querying user data: {e}")
        result = None
    finally:
        connection.close()
    
    if result:
        stored_password_hash = result[0]
        # Use bcrypt to check the password
        return bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8'))
    
    return False
