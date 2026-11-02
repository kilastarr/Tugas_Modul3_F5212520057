import hashlib
import mysql.connector
from config.database import Database

class UserModel:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        hashed_pw = self.hash_password(password)
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT id_user, username, role FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, hashed_pw))
        user = cursor.fetchone()
        cursor.close()
        return user

    def register_user(self, username, password, role="anggota"):
        hashed_pw = self.hash_password(password)
        cursor = self.conn.cursor()
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (username, hashed_pw, role))
            self.conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error Register: {err}")
            cursor.close()
            return False