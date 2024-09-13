from Database_config.db_settings import Database, execute_query
from Decorator.decorator import log_decorator
from Utilits.queries_for_expense import ExpenseManager
from Utilits.queries_for_contractors import ContractorManager

expense = ExpenseManager()
contractor = ContractorManager()


class TenderManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def insert_tender(self):
        """
        Insert a new tender into the tender table
        """
        try:
            expense.view_expenses()
            choice = int(input("Choose your interest: "))
            expense_id = choice
            tender_description = input("Enter the tender description: ")
            contractor.view_contractors()
            contractor_id = int(input("Enter the contractor ID: "))

            query = '''
                    INSERT INTO tender (expense_id, tender_description, contractor_id)
                    VALUES (%s, %s, %s);
                    '''
            values = (expense_id, tender_description, contractor_id)
            execute_query(query, values)
            print("Tender added successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while inserting tender: {str(e)}")
            return False

    @log_decorator
    def update_tender(self):
        """
        Update an existing tender in the tender table based given tender ID
        """
        try:
            tender_id = input("Enter the tender ID: ").strip()
            new_tender_description = input("Enter new tender description: ")
            new_contractor_id = input("Enter new contractor ID: ")

            query = '''UPDATE tender SET tender_description = %s, contractor_id = %s WHERE tender_id = %s'''
            params = (new_tender_description, new_contractor_id, tender_id)
            execute_query(query, params)
            print("Tender updated successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while updating tender: {str(e)}")
            return False

    @log_decorator
    def delete_tender(self):
        """
        Delete a tender from the tender table based on the given tender ID
        """
        try:
            tender_id = input("Enter the tender ID: ").strip()

            query = "DELETE FROM tender WHERE tender_id = %s"
            execute_query(query, (tender_id,))
            print("Tender deleted successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while deleting tender: {str(e)}")
            return False

    @log_decorator
    def view_tenders(self):
        """
        View all tenders in the tender table
        """
        try:
            query = "SELECT * FROM tender"
            result = execute_query(query)
            if result:
                print("Tenders:")
                for row in result:
                    print(
                        f"ID: {row[0]}, Expense ID: {row[1]}, Description: {row[2]},"
                        f" Contractor ID: {row[3]}")
                return True
            else:
                print("No tenders found.")
                return False
        except Exception as e:
            print(f"An error occurred while viewing tenders: {str(e)}")
            return False

    @log_decorator
    def show_active_tenders(self):

        query = '''
            SELECT e.expense_id, b.budget_name, d.direction_name, r.region_name, dis.name, e.amount
            FROM expenses e JOIN budgets b ON e.budget_id = b.budget_id
            JOIN directions d ON e.direction_id = d.direction_id
            JOIN region r ON e.region_id = r.region_id
            JOIN district dis ON e.district_id = dis.district_id ;'''
        result = execute_query(query, fetch='all')
        print('Active tenders:')
        for row in result:
            print(
                f'Expense ID: {row[0]}, Budget Name: {row[1]}, Direction Name: {row[2]}, Region Name: {row[3]}, '
                f'District Name: {row[4]}, Amount: {row[5]}')
            return True
