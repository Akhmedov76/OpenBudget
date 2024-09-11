import threading

from Auth.auth import Auth
from Decorator.decorator import log_decorator
from Utilits.models import CreateTable
from Utilits.queries import QueryManager

auth = Auth()
table = CreateTable()
query_manager = QueryManager()


@log_decorator
def view_auth_menu():
    print("""
1. Register
2. Login
3. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if auth.register():
            view_auth_menu()
        view_auth_menu()
    elif choice == 2:
        result_login = auth.login()
        if not result_login['is_login']:
            view_auth_menu()
        elif result_login['role'] == 'admin':
            view_admin_menu()
        elif result_login['role'] == 'user':
            view_user_menu()
    elif choice == 3:
        print("Goodbye!")
        auth.logout()
    else:
        print("Invalid choice. Please try again.")
        view_auth_menu()


@log_decorator
def view_admin_menu():
    print("""

1. Budget management
2. Expense management
3. Tender management
4. Manage statistics
5. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_budget_menu()
        view_admin_menu()
    elif choice == 2:
        view_expenses_menu()
        view_admin_menu()
    elif choice == 3:
        view_tender_menu()
        view_admin_menu()
    elif choice == 4:
        view_statistics_menu()
        view_admin_menu()
    elif choice == 5:
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice. Please try again.")
        view_admin_menu()


@log_decorator
def view_budget_menu():
    print("""
1. Show all budgets
2. Add a new budget
3. Edit a budget
4. Delete a budget
5. Declaring the season open
6. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        query_manager.view_budgets()
        view_budget_menu()
    elif choice == 2:
        query_manager.insert_budget()
        view_budget_menu()
    elif choice == 3:
        query_manager.update_budget()
        view_budget_menu()
    elif choice == 4:
        query_manager.delete_budget()
        view_budget_menu()
    elif choice == 5:
        query_manager.declaring_season_open()
        view_budget_menu()
    elif choice == 6:
        print("Goodbye!")
        view_admin_menu()
    else:
        print("Invalid choice. Please try again.")
        view_budget_menu()


@log_decorator
def view_expenses_menu():
    print("""
1. Show all expenses
2. Add a new expense
3. Edit an expense
4. Delete an expense
5. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        query_manager.view_expenses()
        view_expenses_menu()
    elif choice == 2:
        query_manager.insert_expense()
        view_expenses_menu()
    elif choice == 3:
        query_manager.update_expense()
        view_expenses_menu()
    elif choice == 4:
        query_manager.delete_expense()
        view_expenses_menu()
    elif choice == 5:
        print("Goodbye!")
        view_admin_menu()
    else:
        print("Invalid choice. Please try again.")
        view_expenses_menu()


@log_decorator
def view_tender_menu():
    print("""
1. Show all tenders
2. Create a new tender
3. Edit a tender
4. Delete a tender
5. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        query_manager.view_tenders()
        view_tender_menu()
    elif choice == 2:
        query_manager.insert_tender()
        view_tender_menu()
    elif choice == 3:
        query_manager.update_tender()
        view_tender_menu()
    elif choice == 4:
        query_manager.delete_tender()
        view_tender_menu()
    elif choice == 5:
        print("Goodbye!")
        view_admin_menu()
    else:
        print("Invalid choice. Please try again.")
        view_tender_menu()


@log_decorator
def view_statistics_menu():
    print("""
1. Show all tenders             
2. District with the most votes         #Eng ko'p taklifga ega ovoz
3. District with the most offers        #Eng ko'p taklifga ega tuman
4. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        query_manager.view_tenders()
        view_statistics_menu()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Goodbye!")
        pass
    else:
        print("Invalid choice. Please try again.")
        view_statistics_menu()


@log_decorator
def view_user_menu():
    print("""
1. Offer for Tender
2. Voting for the tender
3. Show active tenders
4. Show my offer
5. Show my 
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice. Please try again.")
        view_user_menu()


if __name__ == "__main__":
    threading.Thread(target=table.create_all_table).start()
    threading.Thread(target=auth.logout).start()
    view_auth_menu()
