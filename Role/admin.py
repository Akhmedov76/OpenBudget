from database_config.db_settings import Database

"""def insert_budget(self, budget_name, total_amount, date_of_admission, end_date, status=False):"""


class AdminManager:
    def __init__(self):
        self.db = Database

    def add_budget(self):
        budget_name = input("Enter budget name: ")
        total_amount = int(input("Enter total amount: "))
        date_of_admission = input("Enter date of admission (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

