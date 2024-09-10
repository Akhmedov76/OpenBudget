from Decorator.decorator import log_decorator
from database_config.db_settings import Database, execute_query


class QueryManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def insert_budget(self, budget_name, total_amount, date_of_admission, end_date, status=False):
        """
        Insert a new budget into the budgets table
        """
        query = '''
        INSERT INTO budgets (budget_name, total_amount, date_of_admission, end_date, status)
        VALUES (%s, %s, %s, %s, %s);
        '''
        params = (budget_name, total_amount, date_of_admission, end_date, status)
        execute_query(query, params)
        return True

    @log_decorator
    def insert_region(self, region_name):
        """
        Insert a new region into the region table
        """
        query = '''
        INSERT INTO region (region_name)
        VALUES (%s);
        '''
        execute_query(query, (region_name,))
        return True

    @log_decorator
    def insert_district(self, name, region_id):
        """
        Insert a new district into the district table
        """
        query = '''
        INSERT INTO district (name, region_id)
        VALUES (%s, %s);
        '''
        params = (name, region_id)
        execute_query(query, params)
        return True

    @log_decorator
    def insert_expense(self, expense_name, amount, date_of_expense, district_id):
        """
        Insert a new expense into the expenses table
        """
        query = '''
        INSERT INTO expenses (expense_name, amount, date_of_expense, district_id)
        VALUES (%s, %s, %s, %s);
        '''
        params = (expense_name, amount, date_of_expense, district_id)
        execute_query(query, params)
        return True

    @log_decorator
    def insert_tender(self, expense_id, tender_description, contractor_id, tender_amount):
        """
        Insert a new tender into the tender table
        """
        query = '''
        INSERT INTO tender (expense_id, tender_description, contractor_id, tender_amount)
        VALUES (%s, %s, %s, %s);
        '''
        params = (expense_id, tender_description, contractor_id, tender_amount)
        execute_query(query, params)
        return True

    @log_decorator
    def insert_contractor(self, contractor_name, contractor_description, contact_person, contact_number, address):
        """
        Insert a new contractor into the contractors table
        """
        query = '''
        INSERT INTO contractors (contractor_name, contractor_description, contact_person, contact_number, address)
        VALUES (%s, %s, %s, %s, %s);
        '''
        params = (contractor_name, contractor_description, contact_person, contact_number, address)
        execute_query(query, params)
        return True

    @log_decorator
    def insert_vote(self, tender_id, user_id, vote_value):
        """
        Insert a new vote into the votes table
        """
        query = '''
        INSERT INTO votes (tender_id, user_id, vote_value)
        VALUES (%s, %s, %s);
        '''
        params = (tender_id, user_id, vote_value)
        execute_query(query, params)
        return True
