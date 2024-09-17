import sqlite3
import bcrypt

def authenticate_user(username, password):
    connection = sqlite3.connect('patient_management.db')
    cursor = connection.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    connection.close()

    if result:
        stored_password_hash = result[0]
        return bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8'))
    return False