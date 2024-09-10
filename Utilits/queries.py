from Decorator.decorator import log_decorator
from database_config.db_settings import execute_query


class CreateTable:
    @log_decorator
    def create_users_table(self):
        """
        Create users table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS users (
           id SERIAL PRIMARY KEY,
           name VARCHAR(255) NOT NULL,
           email VARCHAR(255) UNIQUE NOT NULL,
           phone_number VARCHAR(20) UNIQUE NOT NULL, 
           password VARCHAR(255) NOT NULL,  
           address VARCHAR(255) NOT NULL,
           status BOOLEAN DEFAULT FALSE,
           role VARCHAR(50) NOT NULL,
           created_at TIMESTAMP NOT NULL
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_all_table(self):
        """
        Create all tables.
        """
        self.create_users_table()

        return True
