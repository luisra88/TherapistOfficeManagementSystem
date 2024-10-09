import os
import sqlite3
from cryptography.fernet import Fernet

# Path to store the encryption key
KEY_FILE_PATH = 'encryption_key.key'

def generate_or_load_key():
    """Generates a new encryption key if not found, otherwise loads it from the key file."""
    if os.path.exists(KEY_FILE_PATH):
        # Read the key from the file
        with open(KEY_FILE_PATH, 'rb') as key_file:
            key = key_file.read()
    else:
        # Generate a new key and save it to the file
        key = Fernet.generate_key()
        with open(KEY_FILE_PATH, 'wb') as key_file:
            key_file.write(key)
    
    return key

# Load or generate the key
KEY = generate_or_load_key()
cipher = Fernet(KEY)

def create_tables():
    connection = sqlite3.connect('patient_management.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        registry_number TEXT PRIMARY KEY,
                        full_name BLOB,
                        chronological_age INTEGER,
                        dob TEXT,
                        mother_name BLOB,
                        father_name BLOB,
                        guardian_name BLOB,
                        address BLOB,
                        phone BLOB,
                        email BLOB,
                        school BLOB,
                        education_region TEXT,
                        municipality TEXT,
                        district TEXT,
                        grade_group TEXT,
                        post TEXT,
                        history_origin INTEGER,
                        people_at_home BLOB,
                        problems_at_home INTEGER,
                        prenatal_history BLOB,
                        perinatal_history BLOB,
                        postnatal_history BLOB,
                        weight_at_birth REAL,
                        size_at_birth REAL,
                        psycholinguistic_dev BLOB,
                        psychomotor_dev BLOB,
                        activity_level BLOB,
                        activity_levels BLOB,
                        current_illnesses BLOB
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER,
                        appointment_date TEXT,
                        FOREIGN KEY(patient_id) REFERENCES patients(id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password_hash TEXT NOT NULL,
                        role TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS documents (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        registry_number TEXT,
                        file_path TEXT NOT NULL,
                        document_type TEXT,
                        created_date TEXT,
                        encrypted BLOB,
                        FOREIGN KEY(registry_number) REFERENCES patients(registry_number)
                      )''')

    connection.commit()
    connection.close()

def encrypt_data(plain_text):
    return cipher.encrypt(plain_text.encode('utf-8'))

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text).decode('utf-8')
if __name__ == "__main__":
    create_tables()

