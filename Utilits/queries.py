import random
import re
import string

from Decorator.decorator import log_decorator
from Database_config.db_settings import Database, execute_query
from Utilits.queries_for_budget import BudgetManager

budget = BudgetManager()


class QueryManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def check_user_is_login(self):
        query = "SELECT * FROM users WHERE status=TRUE"
        result = execute_query(query, fetch="one")
        return result['id']

    @log_decorator
    def get_user_email(self):
        query = "SELECT email FROM users WHERE status=TRUE"
        result = execute_query(query, fetch="one")
        return result['email']

    @log_decorator
    def show_all_votes(self):
        query = '''
            SELECT COUNT(vote_value) AS votesa
            FROM votes '''
        result = execute_query(query, fetch='all')
        for row in result:
            print(f'Total votes: {row[0]}\n')
        return True

    @log_decorator
    def show_all_my_votes(self):
        query = f'''
                SELECT v.vote_id, t.tender_description, u.name
                FROM votes v JOIN tender t on v.vote_id = t.tender_id
                JOIN users u on v.user_id = u.id;'''
        result = execute_query(query, fetch='all')
        print('All my votes:')
        for row in result:
            print(f'Vote ID: {row[0]}, Tender Name: {row[1]}, User Name: {row[2]}')
            return True

    @log_decorator
    def show_all_offers_information(self):
        query = '''
            SELECT o.offer_id, b.budget_name, t.tender_description, r.region_name, d.name, o.offer_description
            FROM offers o JOIN budgets b ON o.budget_id = b.budget_id
            JOIN tender t ON o.tender_id = t.tender_id
            JOIN region r ON o.region_id = r.region_id
            JOIN district d ON o.district_id = d.district_id WHERE EXISTS (
            SELECT 1 FROM users u
            WHERE u.id = o.user_id
        );'''
        result = execute_query(query, fetch='all')
        print('All offers information:')
        for row in result:
            print(
                f'ID: {row[0]}, Season Name: {row[1]}, Tender Name: {row[2]},\nRegion Name: {row[3]}, District Name: {row[4]}, '
                f'Description: {row[5]}')
            return True

    @log_decorator
    def count_offer(self):
        query = '''
                SELECT d.district_id, d.name AS district_name, COUNT(o.offer_id) AS offer_count
                FROM offers o
                JOIN district d ON o.district_id = d.district_id
                GROUP BY d.district_id, d.name
                ORDER BY offer_count DESC
                LIMIT 1; '''
        result = execute_query(query, fetch='one')
        if result:
            print(
                f'District with the most offers: District ID: {result[0]}, District Name: {result[1]}, Offer Count: {result[2]}')
            return True

    @log_decorator
    def declaring_season_open(self):
        """
        Declare a season open for a budget by setting the is_open flag to True
        """
        try:
            budget.view_budgets()
            budget_id = input("Enter the budget ID: ").strip()

            query = "UPDATE budgets SET status = TRUE WHERE budget_id = %s"
            execute_query(query, (budget_id,))
            print("Season open for budget successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while declaring season open: {str(e)}")
            return False


def validate_phone_number(phone_number):
    pattern = r'^\+?[\d\s\-\(\)]{9,15}$'

    if re.match(pattern, phone_number):
        return True
    else:
        return False


@log_decorator
def generate_code(self):
    for i in range(1000, 9999):
        code = f"{i}"
        return code
