import threading

from Auth.auth import Auth

from Decorator.decorator import log_decorator

from Utilits.models import CreateTable
from Utilits.queries import QueryManager
from Utilits.queries_for_tender import TenderManager
from Utilits.queries_for_budget import BudgetManager
from Utilits.queries_for_expense import ExpenseManager
from Utilits.queries_for_directions import DirectionManager
from Utilits.queries_for_offer import OfferManager
from Utilits.queries_for_votes import VoteManager

auth = Auth()
table = CreateTable()
vote_manager = VoteManager()
query_manager = QueryManager()
offer_manager = OfferManager()
tender_manager = TenderManager()
budget_manager = BudgetManager()
expense_manager = ExpenseManager()
direction_manager = DirectionManager()


@log_decorator
def view_auth_menu():
    print("""
1. Register
2. Login
3. Exit
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

1. Season management
2. Direction management
3. Expense management
4. Tender management
5. Manage statistics
6. The total number of votes for the tender
7. Exit the program and return to the auth menu
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_budget_menu()
        view_admin_menu()
    elif choice == 2:
        view_directions_menu()
        view_admin_menu()
    elif choice == 3:
        view_expenses_menu()
        view_admin_menu()
    elif choice == 4:
        view_tender_menu()
        view_admin_menu()
    elif choice == 5:
        view_statistics_menu()
        view_admin_menu()
    elif choice == 6:
        tender_manager.show_active_tenders()
        query_manager.show_all_votes()
        view_admin_menu()
    elif choice == 7:
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice. Please try again.")
        view_admin_menu()


def view_directions_menu():
    print("""
1. Show all directions
2. Add directions
3. Edit directions
4. Delete directions
5. Exit the program and return to the admin menu
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        direction_manager.view_directions()
        view_directions_menu()
    if choice == 2:
        direction_manager.insert_directions()
        view_directions_menu()
    elif choice == 3:
        direction_manager.update_direction()
        view_directions_menu()
    elif choice == 4:
        direction_manager.delete_direction()
        view_directions_menu()
    elif choice == 5:
        print("Goodbye!")
        view_admin_menu()
    else:
        print("Invalid choice. Please try again.")
        view_directions_menu()


@log_decorator
def view_budget_menu():
    print("""
1. Show all season
2. Add a new season
3. Edit a season
4. Delete a season
5. Exit the program and return to the admin menu 
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        budget_manager.view_budgets()
        view_budget_menu()
    elif choice == 2:
        budget_manager.insert_budget()
        view_budget_menu()
    elif choice == 3:
        budget_manager.update_budget()
        view_budget_menu()
    elif choice == 4:
        budget_manager.delete_budget()
        view_budget_menu()
    elif choice == 5:
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
5. Exit the program and return to the admin menu
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        expense_manager.view_expenses()
        view_expenses_menu()
    elif choice == 2:
        expense_manager.insert_expense()
        view_expenses_menu()
    elif choice == 3:
        expense_manager.update_expense()
        view_expenses_menu()
    elif choice == 4:
        expense_manager.delete_expense()
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
5. Exit the program and return to the admin menu
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tender_manager.view_tenders()
        view_tender_menu()
    elif choice == 2:
        tender_manager.insert_tender()
        view_tender_menu()
    elif choice == 3:
        tender_manager.update_tender()
        view_tender_menu()
    elif choice == 4:
        tender_manager.delete_tender()
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
2. District with the most offers 
3. Exit the program with the most auth menu
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tender_manager.view_tenders()
        view_statistics_menu()
    elif choice == 2:
        query_manager.count_offer()
        view_statistics_menu()
    elif choice == 3:
        print("Goodbye!")
        view_auth_menu()
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
5. Show my vote
6. The total number of votes for the tender
7. Exit the program and return to the auth menu
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        offer_manager.insert_offer_table()
        view_user_menu()
    elif choice == 2:
        vote_manager.insert_votes()
        view_user_menu()
    elif choice == 3:
        tender_manager.show_active_tenders()
        view_user_menu()
    elif choice == 4:
        query_manager.show_all_offers_information()
        view_user_menu()
    elif choice == 5:
        query_manager.show_all_my_votes()
        view_user_menu()
    elif choice == 6:
        query_manager.show_all_offers_information()
        query_manager.show_all_votes()
        view_user_menu()
    elif choice == 7:
        print("Goodbye!")
        view_auth_menu()
    else:
        print("Invalid choice. Please try again.")
        view_user_menu()


if __name__ == "__main__":
    threading.Thread(target=table.create_all_table).start()
    threading.Thread(target=auth.logout).start()
    view_auth_menu()
