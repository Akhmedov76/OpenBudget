from Database_config.db_settings import execute_query, Database
from Decorator.decorator import log_decorator


class DirectionManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def insert_directions(self):
        try:
            direct_name = input('Enter direction name: ').capitalize().strip()
            query = '''
                INSERT INTO directions (direction_name) VALUES (%s);
            '''
            params = (direct_name,)
            execute_query(query, params)
            print('Directions inserted successfully')
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while inserting tender: {str(e)}")
            return False

    @log_decorator
    def update_direction(self):
        try:
            direction_id = input('Enter direction ID to update: ')
            new_direct_name = input('Enter new direction name: ')
            query = '''
                UPDATE directions SET direction_name = %s WHERE direction_id = %s;
            '''
            params = (new_direct_name, direction_id)
            execute_query(query, params)
            print('Direction updated successfully')
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"An error occurred while updating direction: {str(e)}")
            return False

    @log_decorator
    def delete_direction(self):
        try:
            direction_id = int(input("Enter direction ID: "))
            query = "DELETE FROM directions WHERE direction_id = %s"
            execute_query(query, (direction_id,))
            print('Direction deleted successfully')
            return True
        except Exception as e:
            print(f"An error occurred while deleting direction: {str(e)}")
            return False

    @log_decorator
    def view_directions(self):
        try:
            query = "SELECT * FROM directions;"
            result = execute_query(query, fetch="all")
            print("Current directions:")
            if result:
                for row in result:
                    print(f"ID: {row[0]}, Direction Name: {row[1]}")
                return True
            else:
                print("No directions found.")
                return False
        except Exception as e:
            print(f"An error occurred while viewing directions: {str(e)}")
            return False
