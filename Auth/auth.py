import datetime
import hashlib
import threading

from Database_config.db_settings import Database, execute_query
from Decorator.decorator import log_decorator
from Email_sender.email import send_mail
from Email_sender.email_checker import check_email
from Utilits.queries import validate_phone_number, generate_code

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "admin"


class Auth:
    def __init__(self):
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__()
        self.__database = Database()

    @log_decorator
    def register(self):
        """
        Register a new user in the system.
        Checks for existing users with the same phone number or email.
        """
        name = input("Enter name: ").capitalize().strip()
        email = input("Enter email: ").strip()
        phone_number = input("Enter phone number: ").strip()
        validate_phone_number(phone_number)
        address = input("Enter address: ").strip()
        gen_pass = generate_code()
        send_mail(email, 'Verification code:', gen_pass)
        confirm_password = input("Enter confirmation password: ").strip()
        if confirm_password != gen_pass:
            print("Passwords do not match.")
            return False
        password = input("Enter password: ").strip()

        hash_pass = hashlib.sha256(password.strip().encode('utf-8')).hexdigest()
        role = 'user'
        try:
            check_email(email)
            subjects = "You logged in"
            message = f"Login: {phone_number}\nPassword: {password}\n"
            threading.Thread(target=send_mail(email, subjects, message)).start()

            query = '''
            SELECT * FROM users WHERE phone_number=%s OR email=%s
            '''
            params = (phone_number, email)
            if execute_query(query, params, fetch='one') is not None:
                print("Phone number or email already exists.")
                return False
            query = '''
            INSERT INTO users (name, email, phone_number, password, address, role)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            params = (name, email, phone_number, hash_pass, address, role)
            execute_query(query, params=params)
            print("Registration successfully")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while registering: {str(e)}")
            return False

    @log_decorator
    def login(self):
        """
        Authenticate a user by checking their email and password.
        Updates the user's login status to True upon successful login.
        """
        try:
            phone_number: str = input("Phone number: ").strip()
            password: str = hashlib.sha256(input("Password: ").strip().encode('utf-8')).hexdigest()

            if phone_number == ADMIN_LOGIN and password == hashlib.sha256(
                    ADMIN_PASSWORD.encode('utf-8')).hexdigest():
                return {'is_login': True, 'role': 'admin'}

            query = '''
            SELECT role FROM users WHERE phone_number=%s AND password=%s
            '''
            params = (phone_number, password)
            user = execute_query(query, params, fetch='one')

            if user is None:
                print("Invalid phone_number or password.")
                return {'is_login': False}

            update_query = 'UPDATE users SET status=TRUE WHERE phone_number=%s'
            execute_query(update_query, params=(phone_number,))

            return {'is_login': True, 'role': user['role']}
        except ValueError:
            print("Invalid input. Please try again.")
            return None
        except IndexError:
            print("Email or password is incorrect.")
            return None
        except Exception as e:
            print(f"An error occurred while logging in: {str(e)}")
            return None

    @log_decorator
    def logout(self):
        """
                Set the login status of all users to False (i.e., log out all users).
        """
        query = 'UPDATE users SET status=FALSE;'
        execute_query(query)
        return True
