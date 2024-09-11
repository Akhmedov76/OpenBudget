from Decorator.decorator import log_decorator
from database_config.db_settings import Database, execute_query


class QueryManager:
    def __init__(self):
        self.db = Database

    def insert_budget(self):
        budget_name = input("Enter the budget name: ")
        total_amount = int(input("Enter the total amount: "))
        date_of_admission = int(input("Enter the date of admission (timestamp): "))

        query = '''
        INSERT INTO budgets (budget_name, total_amount, date_of_admission)
        VALUES (%s, %s, %s, %s, %s);
        '''
        params = (budget_name, total_amount, date_of_admission)
        execute_query(query, params)
        print("Budget added successfully!")
        return True

    @log_decorator
    def update_budget(self):
        budget_id = input("Enter the budget ID: ").strip()
        new_total_amount = input("Enter new total amount: ")

        query = '''UPDATE budgets SET total_amount = %s WHERE budget_id = %s'''
        params = (new_total_amount, budget_id)
        execute_query(query, params)
        print("Budget updated successfully!")
        return True

    @log_decorator
    def delete_budget(self):
        budget_id = input("Enter the budget ID: ").strip()

        query = "DELETE FROM budgets WHERE budget_id = %s"
        execute_query(query, (budget_id,))
        print("Budget deleted successfully!")
        return True

    @log_decorator
    def view_budgets(self):
        query = "SELECT * FROM budgets"
        result = execute_query(query)
        print("Budgets:")
        for row in result:
            print(row)
        return True

    def insert_expense(self):
        expense_name = input("Enter the expense name: ")
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

    @log_decorator
    def update_expense(self):
        expense_id = input("Enter the expense ID: ").strip()
        new_expense_name = input("Enter new expense name: ")
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

    @log_decorator
    def delete_expense(self):
        expense_id = input("Enter the expense ID: ").strip()

        query = "DELETE FROM expenses WHERE expense_id = %s"
        execute_query(query, (expense_id,))
        print("Expense deleted successfully!")
        return True

    @log_decorator
    def view_expenses(self):
        query = "SELECT * FROM expenses"
        result = execute_query(query)
        print("Expenses:")
        for row in result:
            print(row)
        return True

    @log_decorator
    def insert_contract_table(self):
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

    @log_decorator
    def insert_contractors(self):
        query = '''INSERT INTO contractors (contractor_name, contractor_description, contact_person, contact_number, address) 
                VALUES 
                ('Ozbekiston Qurilish', 'Qurilish materiallari va xizmatlari', 'Javlonbek S', '+998901234567', 'Toshkent, Chilonzor tumani, 123-uy'),
                ('SamDant', 'Samarkand viloyati uchun dant va qurilish xizmatlari', 'Mukhammadbek D', '+998901234568', 'Samarkand, Bobur kochasi, 45-uy'),
                ('TechnoBuild', 'Yangi texnologiyalar bilan qurilish', 'Nilufar A', '+998901234569', 'Buxoro, Mustaqillik kochasi, 78-uy'),
                ('Toshkent Elektronika', 'Elektronika va avtomatlashtirish', 'Azamat J', '+998901234570', 'Toshkent, Yakkasaroy tumani, 34-uy'),
                ('Qurilish Materiallari', 'Turli qurilish materiallari', 'Zebo M', '+998901234571', 'Fargona, Gofur Gulom kochasi, 12-uy');'''
        execute_query(query, )
        return True

    @log_decorator
    def update_contractors(self):
        contractor_id = input("Enter the contractor ID: ").strip()
        new_contractor_name = input("Enter new contractor name: ")
        new_contractor_description = input("Enter new contractor description: ")
        new_contact_person = input("Enter new contractor contact person: ")
        new_contact_number = input("Enter new contractor contact number: ")
        new_address = input("Enter new contractor address: ")

        query = '''UPDATE contractors SET contractor_name = %s, contractor_description = %s, contact_person = %s,
                   contact_number = %s, address = %s WHERE contractor_id = %s'''
        params = (new_contractor_name, new_contractor_description, new_contact_person, new_contact_number, new_address,
                  contractor_id)
        execute_query(query, params)
        print("Contractor updated successfully!")
        return True

    @log_decorator
    def delete_contractors(self):
        contractor_id = input("Enter the contractor ID: ").strip()

        query = "DELETE FROM contractors WHERE contractor_id = %s"
        execute_query(query, (contractor_id,))
        print("Contractor deleted successfully!")
        return True

    @log_decorator
    def view_contractors(self):
        query = "SELECT * FROM contractors"
        result = execute_query(query)
        print("Contractors:")
        for row in result:
            print(row)
        return True

    @log_decorator
    def insert_tender(self):
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

    @log_decorator
    def update_tender(self):
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

    @log_decorator
    def delete_tender(self):
        tender_id = input("Enter the tender ID: ").strip()

        query = "DELETE FROM tender WHERE tender_id = %s"
        execute_query(query, (tender_id,))
        print("Tender deleted successfully!")
        return True

    @log_decorator
    def view_tenders(self):
        query = "SELECT * FROM tender"
        result = execute_query(query)
        print("Tenders:")
        for row in result:
            print(row)
        return True

    @log_decorator
    def insert_votes(self):
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

    @log_decorator
    def update_votes(self):
        vote_id = input("Enter the vote ID: ").strip()
        new_vote_value = int(input("Enter new vote value (1-5): "))

        query = '''UPDATE votes SET vote_value = %s WHERE vote_id = %s'''
        params = (new_vote_value, vote_id)
        execute_query(query, params)
        print("Vote updated successfully!")
        return True

    @log_decorator
    def delete_votes(self):
        vote_id = input("Enter the vote ID: ").strip()

        query = "DELETE FROM votes WHERE vote_id = %s"
        execute_query(query, (vote_id,))
        print("Vote deleted successfully!")
        return True

    @log_decorator
    def view_votes(self):
        query = "SELECT * FROM votes"
        result = execute_query(query)
        print("Votes:")
        for row in result:
            print(row)
        return True
