import psycopg2
from psycopg2 import sql
from .db_setup import connect_to_database
from ..utils.db_config import load_db_config
from psycopg2.extras import RealDictCursor

# Define the required NOT NULL fields for validation
NEW_PATIENT_REQUIRED_FIELDS = {'full_name', 'registry_number', 'date_of_birth' }
VALID_PATIENT_INFO_SECTIONS = {'evo_development', 'prenatal_history', 'postnatal_history','development', 'illnesses', 'scholar_history'}

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

def create_or_update_patient(patient_info):
    """Insert a new patient or update an existing one in the database."""
    connection = None
    patient_id = None

    try:
        # Load database configuration and connect
        db_config = load_db_config()
        db_name = db_config['db_name']
        connection = connect_to_database(db_name)
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Step 1: Check if the patient already exists based on registry_number
        registry_number = patient_info.get('registry_number')
        if not registry_number:
            raise ValueError("Missing required field: 'registry_number'")

        cursor.execute(
            "SELECT patient_id FROM patients WHERE registry_number = %s;",
            (registry_number,)
        )
        existing_patient = cursor.fetchone()

        # Step 2: If patient does not exist, validate all required fields
        if not existing_patient:
            missing_fields = NEW_PATIENT_REQUIRED_FIELDS - patient_info.keys()
            if missing_fields:
                raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        # Step 3: Prepare the columns, placeholders, and values for insertion/upsert
        columns = ', '.join(patient_info.keys())
        placeholders = ', '.join(['%s'] * len(patient_info))
        values = tuple(patient_info.values())

        # Step 4: Build the upsert query with ON CONFLICT clause
        query = f"""
        INSERT INTO patients ({columns})
        VALUES ({placeholders})
        ON CONFLICT (registry_number) 
        DO UPDATE SET {', '.join([f"{col} = EXCLUDED.{col}" for col in patient_info.keys()])}
        RETURNING patient_id;
        """
        cursor.execute(query, values)

        # Fetch the generated or existing patient_id
        patient_id = cursor.fetchone()['patient_id']

        # Commit the transaction
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while creating/updating patient: {error}")
        if connection:
            connection.rollback()  # Roll back on error
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return patient_id


def get_patient_by_registry_number(registry_number):
    """Fetch the patient_id of a patient by their registry number."""
    connection = None
    patient_id = None

    try:
        # Load database configuration and connect
        db_config = load_db_config()
        db_name = db_config['db_name']
        connection = connect_to_database(db_name)
        cursor = connection.cursor()

        # Query to fetch the patient_id by registry number
        query = "SELECT patient_id FROM patients WHERE registry_number = %s;"
        cursor.execute(query, (registry_number,))

        result = cursor.fetchone()
        if result:
            patient_id = result[0]  # Extract the patient_id

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error fetching patient_id: {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return patient_id

def create_or_update_patient_info_section(patient_info_section, registry_number, patient_info):
    if patient_info_section not in VALID_PATIENT_INFO_SECTIONS:
        raise ValueError(f"Invalid section: {patient_info_section}")

    """Insert or update a section of a patient's data."""
    connection = None

    try:
        # Get the patient_id using the provided registry_number
        patient_id = get_patient_by_registry_number(registry_number)
        if not patient_id:
            raise ValueError(f"No patient found with registry number: {registry_number}")

        # Load database configuration and connect
        db_config = load_db_config()
        db_name = db_config['db_name']
        connection = connect_to_database(db_name)
        cursor = connection.cursor()

        # Prepare the columns and values for upsert
        columns = ', '.join(patient_info.keys())
        placeholders = ', '.join(['%s'] * len(patient_info))
        values = tuple(patient_info.values()) + (patient_id,)

        # Build the dynamic SQL query with ON CONFLICT for upsert
        query = f"""
        INSERT INTO {patient_info_section} ({columns}, patient_id)
        VALUES ({placeholders}, %s)
        ON CONFLICT (patient_id) 
        DO UPDATE SET {', '.join([f"{col} = EXCLUDED.{col}" for col in patient_info.keys()])}
        RETURNING patient_id;
        """
        cursor.execute(query, values)

        # Fetch the updated or inserted patient_id
        updated_patient_id = cursor.fetchone()[0]

        # Commit the transaction
        connection.commit()

        print(f"Section '{patient_info_section}' successfully created/updated for patient ID: {updated_patient_id}")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error in create_or_update_patient_section: {error}")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

