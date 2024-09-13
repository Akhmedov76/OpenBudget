from Database_config.db_settings import execute_query, Database
from Decorator.decorator import log_decorator
from Utilits.queries_for_budget import BudgetManager

budget = BudgetManager()


class OfferManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def insert_offer_table(self):
        budget.view_budgets()
        budget_id = int(input("Enter a budget ID: "))
        if not budget.check_budgets(budget_id):
            print("Budget not found or inactive.")
            return self.insert_offer_table()
        else:
            tender_id = int(input("Enter a tender ID: "))
        region_id = int(input("Enter a region ID: "))
        district_id = int(input("Enter a district ID: "))
        direction_id = input("Enter a direction ID: ")
        user_id = int(input("Enter a user ID: "))
        offer_description = input("Enter a description of the offer to insert into the database: ")
        query = '''
        INSERT INTO offers (budget_id, tender_id, region_id, district_id, direction_id, user_id, offer_description) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        params = (budget_id, tender_id, region_id, district_id, direction_id, user_id, offer_description)
        execute_query(query, params)
        print('Offer inserted successfully')
        return True

    @log_decorator
    def update_offer(self):
        offer_id = int(input("Enter an offer ID to update: "))
        new_budget_id = int(input("Enter a new budget ID: "))
        new_tender_id = int(input("Enter a new tender ID: "))
        new_region_id = int(input("Enter a new region ID: "))
        new_district_id = int(input("Enter a new district ID: "))
        new_direction_name = input("Enter a new direction name: ")
        new_user_id = int(input("Enter a new user ID: "))
        offer_description = input("Enter a new description for the offer: ")
        query = '''
        UPDATE offers SET budget_id=%s, tender_id=%s, region_id=%s, district_id=%s, direction_name=%s, user_id=%s,
         offer_description=%s, WHERE offer_id=%s
        '''
        params = (new_budget_id, new_tender_id, new_region_id, new_district_id, new_direction_name, new_user_id,
                  offer_description, offer_id)
        execute_query(query, params)
        print('Offer updated successfully')
        return True

    @log_decorator
    def delete_offer(self):
        offer_id = int(input("Enter an offer ID to delete: "))
        query = '''
        DELETE FROM offers WHERE offer_id=%s
        '''
        params = (offer_id,)
        execute_query(query, params)
        print('Offer deleted successfully')
        return True

    @log_decorator
    def view_offers(self):
        query = '''
        SELECT * FROM offers
        '''
        result = execute_query(query)
        print('Offers:')
        for row in result:
            print(
                f'Offer ID: {row[0]}, Budget ID: {row[1]}, Tender ID: {row[2]}, Region ID: {row[3]}, District ID: {row[4]}, '
                f'Direction Name: {row[5]}, User ID: {row[6]}, Offer Description: {row[7]}')
        return True
