from Decorator.decorator import log_decorator
from database_config.db_settings import Database, execute_query


class QueryManager:
    def __init__(self):
        self.db = Database

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
    def declaring_season_open(self):
        """
        Declare a season open for a budget by setting the is_open flag to True
        """
        try:
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
                        f"Budget ID: {row[0]}\n, Budget Name: {row[1]}, Total Amount: {row[2]}, Date of Admission: {row[3]},"
                        f" Status: {row[4]}")
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

    def insert_expense(self):
        """
        Insert a new expense into the expenses table
        """
        try:
            expense_name = input("Enter the expense name: ").capitalize().strip()
            region_id = int(input("Enter the region ID: "))
            district_id = input("Enter the district ID (or leave blank if not applicable): ")
            if not district_id:
                district_id = None
            else:
                district_id = int(district_id)
            amount = int(input("Enter the amount: "))

            query = '''
                INSERT INTO expenses (expense_name, region_id, district_id, amount)
                VALUES (%s, %s, %s, %s);
                '''
            values = (expense_name, region_id, district_id, amount)
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
            new_expense_name = input("Enter new expense name: ").capitalize().strip()
            new_region_id = int(input("Enter new region ID: "))
            new_district_id = input("Enter new district ID (or leave blank if not applicable): ")
            if not new_district_id:
                new_district_id = None
            else:
                new_district_id = int(new_district_id)
            new_amount = int(input("Enter new amount: "))

            query = '''UPDATE expenses SET expense_name = %s, region_id = %s, district_id = %s, amount = %s 
                           WHERE expense_id = %s'''
            params = (new_expense_name, new_region_id, new_district_id, new_amount, expense_id)
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
                        f"Expense ID: {row[0]},\nExpense Name: {row[1]}, Region ID: {row[2]}, District ID: {row[3]},"
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

    @log_decorator
    def insert_contract_table(self):
        """
        Insert a new contract table into the contract_tables table
        """
        try:
            contractor_name = input("Enter the contractor name: ")
            contractor_description = input("Enter the contractor description: ")
            contact_person = input("Enter the contact person: ")
            contact_number = input("Enter the contact number: ")
            address = input("Enter the address: ")

            query = '''
                        INSERT INTO contractors (contractor_name, contractor_description, contact_person, contact_number, address)
                        VALUES (%s, %s, %s, %s, %s);
                        '''
            values = (contractor_name, contractor_description, contact_person, contact_number, address)
            execute_query(query, values)
            print("Contractor added successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while inserting contractor: {str(e)}")
            return False

    @log_decorator
    def insert_contractors(self):
        """
        Insert multiple contractors into the contractors table
        """
        try:
            query = '''INSERT INTO contractors (contractor_name, contractor_description, contact_person, contact_number, address) 
                        VALUES 
                        ('Ozbekiston Qurilish', 'Qurilish materiallari va xizmatlari', 'Javlonbek S', '+998901234567', 'Toshkent, Chilonzor tumani, 123-uy'),
                        ('SamDant', 'Samarkand viloyati uchun dant va qurilish xizmatlari', 'Mukhammadbek D', '+998901234568', 'Samarkand, Bobur kochasi, 45-uy'),
                        ('TechnoBuild', 'Yangi texnologiyalar bilan qurilish', 'Nilufar A', '+998901234569', 'Buxoro, Mustaqillik kochasi, 78-uy'),
                        ('Toshkent Elektronika', 'Elektronika va avtomatlashtirish', 'Azamat J', '+998901234570', 'Toshkent, Yakkasaroy tumani, 34-uy'),
                        ('Qurilish Materiallari', 'Turli qurilish materiallari', 'Zebo M', '+998901234571', 'Fargona, Gofur Gulom kochasi, 12-uy');'''
            execute_query(query, )
            print("Contractors added successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while inserting contractors: {str(e)}")
            return False

    @log_decorator
    def update_contractors(self):
        """
        Update an existing contractor in the contractors table based given contractor ID
        """
        try:
            contractor_id = input("Enter the contractor ID: ").strip()
            new_contractor_name = input("Enter new contractor name: ")
            new_contractor_description = input("Enter new contractor description: ")
            new_contact_person = input("Enter new contractor contact person: ")
            new_contact_number = input("Enter new contractor contact number: ")
            new_address = input("Enter new contractor address: ")

            query = '''UPDATE contractors SET contractor_name = %s, contractor_description = %s, contact_person = %s,
                           contact_number = %s, address = %s WHERE contractor_id = %s'''
            params = (
                new_contractor_name, new_contractor_description, new_contact_person, new_contact_number, new_address,
                contractor_id)
            execute_query(query, params)
            print("Contractor updated successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while updating contractor: {str(e)}")
            return False

    @log_decorator
    def delete_contractors(self):
        """
        Delete a contractor from the contractors table based on the given contractor ID
        """
        try:
            contractor_id = input("Enter the contractor ID: ").strip()

            query = "DELETE FROM contractors WHERE contractor_id = %s"
            execute_query(query, (contractor_id,))
            print("Contractor deleted successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while deleting contractor: {str(e)}")
            return False

    @log_decorator
    def view_contractors(self):
        """
        View all contractors in the contractors table
        """
        try:
            query = "SELECT * FROM contractors"
            result = execute_query(query)
            print("Contractors:")
            for row in result:
                print(row)
            return True
        except Exception as e:
            print(f"An error occurred while viewing contractors: {str(e)}")
            return False

    @log_decorator
    def insert_tender(self):
        """
        Insert a new tender into the tender table
        """
        try:
            expense_id = int(input("Enter the expense ID: "))
            tender_description = input("Enter the tender description: ")
            contractor_id = int(input("Enter the contractor ID: "))
            tender_amount = int(input("Enter the tender amount: "))

            query = '''
                INSERT INTO tender (expense_id, tender_description, contractor_id, tender_amount)
                VALUES (%s, %s, %s, %s);
                '''
            values = (expense_id, tender_description, contractor_id, tender_amount)
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
            new_contractor_id = int(input("Enter new contractor ID: "))
            new_tender_amount = int(input("Enter new tender amount: "))

            query = '''UPDATE tender SET tender_description = %s, contractor_id = %s, tender_amount = %s 
                           WHERE tender_id = %s'''
            params = (new_tender_description, new_contractor_id, new_tender_amount, tender_id)
            execute_query(query, params)
            print("Tender updated successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False

    @log_decorator
    def delete_tender(self):
        """
        Delete a tender from the tender table based given tender ID
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
            result = execute_query(query, fetch="all")
            if result:
                print("Tenders:")
                for row in result:
                    print(
                        f"Tender ID: {row[0]},\nExpense ID: {row[1]}, Tender description: {row[2]}, Contractor: {row[3]},"
                        f"Tender amount: {row[4]}")
                    print(row)
                return True
        except Exception as e:
            print(f"An error occurred while viewing tenders: {str(e)}")
            return False

    @log_decorator
    def insert_votes(self):
        """
        Insert a new vote into the votes table
        """
        try:
            tender_id = int(input("Enter the tender ID: "))
            user_id = int(input("Enter the user ID: "))
            vote_value = int(input("Enter the vote value (1-5): "))

            query = '''
                INSERT INTO votes (tender_id, user_id, vote_value)
                VALUES (%s, %s, %s);
                '''
            values = (tender_id, user_id, vote_value)
            execute_query(query, values)
            print("Vote added successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False

    @log_decorator
    def update_votes(self):
        """
        Update an existing vote in the votes table based given vote ID
        """
        try:
            vote_id = input("Enter the vote ID: ").strip()
            new_vote_value = int(input("Enter new vote value (1-5): "))

            query = '''UPDATE votes SET vote_value = %s WHERE vote_id = %s'''
            params = (new_vote_value, vote_id)
            execute_query(query, params)
            print("Vote updated successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while updating vote: {str(e)}")
            return False

    @log_decorator
    def delete_votes(self):
        """
        Delete a vote from the votes table based given vote ID
        """
        try:
            vote_id = input("Enter the vote ID: ").strip()

            query = "DELETE FROM votes WHERE vote_id = %s"
            execute_query(query, (vote_id,))
            print("Vote deleted successfully!")
            return True
        except Exception as e:
            print(f"An error occurred while deleting vote: {str(e)}")
            return False

    @log_decorator
    def view_votes(self):
        """
        View all votes in the votes table
        """
        try:
            query = "SELECT * FROM votes"
            result = execute_query(query)
            print("Votes:")
            for row in result:
                print(row)
            return True
        except Exception as e:
            print(f"An error occurred while viewing votes: {str(e)}")
            return False
