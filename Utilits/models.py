from Decorator.decorator import log_decorator
from Database_config.db_settings import execute_query
from Regions_and_district.region import region_name
from Regions_and_district.district import district_name
from Utilits.queries import QueryManager

query_manager = QueryManager()


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
            total_amount FLOAT NOT NULL,
            date_of_admission DATE NOT NULL,
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
            budget_id BIGINT REFERENCES budgets(budget_id),
            direction_id BIGINT REFERENCES directions(direction_id),
            region_id BIGINT NOT NULL REFERENCES region(region_id),
            district_id BIGINT REFERENCES district(district_id),
            amount BIGINT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
            address VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
            contractor_id BIGINT REFERENCES contractors(contractor_id)
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
            vote_value INTEGER DEFAULT 1 NOT NULL
        );'''
        execute_query(query)
        return True

    @log_decorator
    def create_direction_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS directions (
            direction_id SERIAL PRIMARY KEY,
            direction_name VARCHAR(255) NOT NULL
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_offer_table(self):
        """
        Create offers table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS offers (
            offer_id SERIAL PRIMARY KEY,
            budget_id BIGINT REFERENCES budgets(budget_id),
            tender_id BIGINT REFERENCES tender(tender_id),
            region_id BIGINT REFERENCES region(region_id),
            district_id BIGINT REFERENCES district(district_id),
            direction_id BIGINT REFERENCES directions(direction_id),
            user_id BIGINT REFERENCES users(id),
            offer_description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );'''
        execute_query(query)
        return True

    @log_decorator
    def tenders_win_table(self):
        """
        Create tenders_win table if it doesn't exist
        """
        query = '''
        CREATE TABLE IF NOT EXISTS winners (
            tender_win_id SERIAL PRIMARY KEY,
            tender_id BIGINT REFERENCES tender(tender_id),
            vote_id BIGINT REFERENCES vote(vote_id)
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
        # region_name()
        self.create_district_table()
        # district_name()
        self.create_direction_table()
        self.create_contractors_table()
        # query_manager.insert_contractors()
        self.create_votes_table()
        self.create_expenses_table()
        self.create_tender_table()
        self.create_offer_table()
        return True
