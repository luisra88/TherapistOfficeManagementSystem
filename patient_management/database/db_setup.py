import sqlite3

def create_tables():
    connection = sqlite3.connect('patient_management.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        contact TEXT,
                        age INTEGER
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
                        patient_id INTEGER,
                        file_path TEXT NOT NULL,
                        encrypted BLOB,
                        FOREIGN KEY(patient_id) REFERENCES patients(id)
                      )''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()