from Database_config.db_settings import Database, execute_query
from Decorator.decorator import log_decorator
from Regions_and_district.region import get_regions
from Utilits.queries_for_budget import BudgetManager
from Utilits.queries_for_directions import DirectionManager

budget = BudgetManager()
direction = DirectionManager()


class ExpenseManager:
    def __init__(self):
        self.database = Database

    @log_decorator
    def insert_expense(self):
        """
        Insert a new expense into the expenses table
        """
        try:
            budget.view_budgets()
            budget_id = input("Enter the budget ID: ").strip()
            direction.view_directions()
            direction_id = input("Enter the direction id: ").strip()
            get_regions()
            region_id = int(input("Enter the region ID: "))
            district_id = input("Enter the district ID (or leave blank if not applicable): ")
            if not district_id:
                district_id = None
            else:
                district_id = int(district_id)
            amount = int(input("Enter the amount: "))

            query = '''
                    INSERT INTO expenses (budget_id, direction_id, region_id, district_id, amount)
                    VALUES (%s,%s, %s, %s, %s);
                    '''
            values = (budget_id, direction_id, region_id, district_id, amount)
            execute_query(query, values)
            print("Expense added successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while inserting expense: {str(e)}")
            return False

    @log_decorator
    def update_expense(self):
        """
        Update an existing expense in the expenses table
        """
        try:
            expense_id = input("Enter the expense ID: ").strip()
            new_direction_id = input("Enter new direction id name: ").strip()
            new_region_id = int(input("Enter new region ID: "))
            new_district_id = input("Enter new district ID (or leave blank if not applicable): ")
            if not new_district_id:
                new_district_id = None
            else:
                new_district_id = int(new_district_id)
            new_amount = int(input("Enter new amount: "))

            query = '''UPDATE expenses SET direction_id = %s, region_id = %s, district_id = %s, amount = %s 
                               WHERE expense_id = %s'''
            params = (new_direction_id, new_region_id, new_district_id, new_amount, expense_id)
            execute_query(query, params)
            print("Expense updated successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while updating expense: {str(e)}")
            return False

    @log_decorator
    def delete_expense(self):
        """
        Delete an expense from the expenses table based on the given expense ID
        """
        try:
            expense_id = input("Enter the expense ID: ").strip()

            query = "DELETE FROM expenses WHERE expense_id = %s"
            execute_query(query, (expense_id,))
            print("Expense deleted successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while deleting expense: {str(e)}")
            return False

    @log_decorator
    def view_expenses(self):
        """
        View all expenses in the expenses table
        """
        try:
            query = "SELECT * FROM expenses"
            result = execute_query(query, fetch="all")
            if result:
                print("Expenses:")
                for row in result:
                    print(
                        f"ID: {row[0]}, Expense Name: {row[1]}, Region ID: {row[2]}, District ID: {row[3]},"
                        f" Amount: {row[4]}")
                return True
            else:
                print("No expenses found.")
                return False
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except KeyError:
            print("Error: Budgets table not found.")
            return False
        except TypeError:
            print("Error: Connection to the database failed.")
            return False
        except Exception as e:
            print(f"An error occurred while viewing budgets: {str(e)}")
        return False
