from Database_config.db_settings import execute_query, Database
from Decorator.decorator import log_decorator


class BudgetManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def insert_budget(self):
        """
        Insert a new budget into the budgets table
        """
        try:
            budget_name = input("Enter the budget name: ")
            total_amount = int(input("Enter the total amount: "))
            date_of_admission = input("Enter the date of admission (timestamp): ")

            query = '''
            INSERT INTO budgets (budget_name, total_amount, date_of_admission)
            VALUES (%s, %s, %s);
            '''
            params = (budget_name, total_amount, date_of_admission)
            execute_query(query, params)
            print("Budget added successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while inserting budget: {str(e)}")
            return False

    @log_decorator
    def update_budget(self):
        """
        Update an existing budget in the budgets table
        """
        try:
            budget_id = input("Enter the budget ID: ").strip()
            new_total_amount = input("Enter new total amount: ")

            query = '''UPDATE budgets SET total_amount = %s WHERE budget_id = %s'''
            params = (new_total_amount, budget_id)
            execute_query(query, params)
            print("Budget updated successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while updating budget: {str(e)}")
            return False

    @log_decorator
    def delete_budget(self):
        """
        Delete a budget from the budgets table based on the given budget ID
        """
        try:
            budget_id = input("Enter the budget ID: ").strip()

            query = "DELETE FROM budgets WHERE budget_id = %s"
            execute_query(query, (budget_id,))
            print("Budget deleted successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while deleting budget: {str(e)}")
            return False



    @log_decorator
    def view_budgets(self):
        """
        View all budgets in the budgets table
        """
        try:
            query = "SELECT * FROM budgets"
            result = execute_query(query, fetch='all')
            if result:
                print("Budgets:")
                for row in result:
                    print(
                        f"Budget ID: {row[0]}, Budget Name: {row[1]}, Total Amount: {row[2]}, Date of Admission: {row[3]},"
                        f" Status: {row[4]}")
                return True
            else:
                print("No budgets found.")
                return True
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

    @log_decorator
    def check_budgets(self, budget_id):
        query = '''
            SELECT * FROM budgets WHERE budget_id = %s AND status = TRUE;
            '''
        params = (budget_id,)
        result = execute_query(query, params, fetch="one")
        if result:
            return True
        else:
            return False
