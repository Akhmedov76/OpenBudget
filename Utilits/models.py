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
           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_budgets_table(self):
        """
        Create budgets table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS budgets (
            budget_id SERIAL PRIMARY KEY,
            budget_name VARCHAR(255) NOT NULL,
            total_amount BIGINT NOT NULL,
            date_of_admission BIGINT NOT NULL,
            end_date BIGINT NOT NULL,
            status BOOLEAN DEFAULT FALSE
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_region_table(self):
        """
        Create region table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS region (
            region_id SERIAL PRIMARY KEY,
            region_name VARCHAR(255) NOT NULL
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_district_table(self):
        """
        Create district table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS district (
            district_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            region_id BIGINT REFERENCES region(region_id)
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_expenses_table(self):
        """
        Create expenses table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id SERIAL PRIMARY KEY,
            expense_name VARCHAR(255) NOT NULL,
            amount BIGINT NOT NULL,
            date_of_expense BIGINT NOT NULL,
            district_id BIGINT REFERENCES district(district_id)
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_contractors_table(self):
        """
        Create contractors table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS contractors (
            contractor_id SERIAL PRIMARY KEY,
            contractor_name VARCHAR(255) NOT NULL,
            contractor_description TEXT NOT NULL,
            contact_person VARCHAR(255) NOT NULL,
            contact_number VARCHAR(20) NOT NULL,
            address VARCHAR(255) NOT NULL
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_tender_table(self):
        """
        Create tender table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS tender (
            tender_id SERIAL PRIMARY KEY,
            expense_id BIGINT REFERENCES expenses(expense_id),
            tender_description TEXT NOT NULL,
            contractor_id BIGINT REFERENCES contractors(contractor_id),
            tender_amount BIGINT NOT NULL
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_votes_table(self):
        """
        Create votes table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS votes (
            vote_id SERIAL PRIMARY KEY,
            tender_id BIGINT REFERENCES tender(tender_id),
            user_id BIGINT REFERENCES users(id),
            vote_value INTEGER NOT NULL
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_all_table(self):
        """
        Create all tables.
        """
        self.create_users_table()
        self.create_budgets_table()
        self.create_region_table()
        self.create_district_table()
        self.create_expenses_table()
        self.create_tender_table()
        self.create_contractors_table()
        self.create_votes_table()
        return True
