import psycopg2
from psycopg2 import sql
from .db_setup import connect_to_database
from ..utils.db_config import load_db_config

def db_load_patients():
    """Retrieve all patients from the patients table."""
    connection = None
    patients = []
    try:
        db_config = load_db_config()
        db_name = db_config['db_name']
        connection = connect_to_database(db_name)
        cursor = connection.cursor()
        
        # Define the query to fetch all patients
        query = "SELECT * FROM patients"
        cursor.execute(query)
        
        # Fetch all patient records
        patients = cursor.fetchall()
        
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while fetching patients: {error}")
    finally:
        if connection is not None:
            connection.close()
    
    return patients
