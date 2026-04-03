from model.db_connections import connect_db
from mysql.connector import Error
import bcrypt


class UserModel:
    @staticmethod
    def login(username, password):
        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor(dictionary=True)

            query = """
            SELECT 
                user_id,
                username, 
                password, 
                role,
                full_name,
                contact_number,
                email,
                is_active
            FROM users 
            WHERE username = %s AND is_active = 1
            """
            cursor.execute(query, (username,))
            user = cursor.fetchone()

            cursor.close()

            if user:
                stored_password = user['password']

                if stored_password.startswith('$2b$'):
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        print(f"Login successful for: {user['username']} (Role: {user['role']})")
                        user['id'] = user['user_id']
                        return user
                else:
                    if password == stored_password:
                        print(f"WARNING: User {username} still has plain text password!")
                        user['id'] = user['user_id']
                        return user

            print(f"Login failed for: {username}")
            return None

        except Error as e:
            print(f"MySQL Error")
            return None
        finally:
            if connection and connection.is_connected():
                connection.close()

    @staticmethod
    def create_user(username, password, role, full_name, contact_number, email):
        connection = None
        try:
            connection = connect_db()
            cursor = connection.cursor()

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

            query = """
            INSERT INTO users (username, password, role, full_name, contact_number, email, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, 1)
            """
            cursor.execute(query, (username, hashed_password.decode('utf-8'), role,
                                   full_name, contact_number, email))
            connection.commit()
            return cursor.lastrowid

        except Error as e:
            print(f"Error creating user: {e}")
            return None
        finally:
            if connection and connection.is_connected():
                connection.close()