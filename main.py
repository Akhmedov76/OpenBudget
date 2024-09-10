def view_auth_menu():
    print("""
1. Register
2. Login
3. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        print("Goodbye!")
        pass
    else:
        print("Invalid choice. Please try again.")
        view_auth_menu()


def view_admin_menu():
    print("""
1. Budget management                        #Byudjetni boshqarish
2. User management
3. Add a new manager
4. Manage income and support                #Daromad va yordamni boshqaring
5. Management of departments and tenders    #Bo'limlar va tenderlarni boshqarish
6. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        print("Goodbye!")
        pass
    else:
        print("Invalid choice. Please try again.")
        view_admin_menu()


def view_budget_menu():
    print("""
1. Add a new budget
2. View budgets
3. Edit a budget
4. Delete a budget
5. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Goodbye!")
        pass
    else:
        print("Invalid choice. Please try again.")
        view_budget_menu()


def view_user_menu():
    print("""
1. Show all tender
2. Voting for the tender
3. Show my tenders
4. Logout 
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
        pass
    else:
        print("Invalid choice. Please try again.")
        view_user_menu()


def view_manager_menu():
    print("""
1. Add a new manager
2. Edit a manager
3. Delete a manager
4. View managers
5. Logout
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        print("Goodbye!")
        pass
    else:
        print("Invalid choice. Please try again.")
        view_manager_menu()
