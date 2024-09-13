from Database_config.db_settings import Database, execute_query
from Decorator.decorator import log_decorator
from Utilits.queries_for_tender import TenderManager
from Utilits.queries import QueryManager

tender = TenderManager()
queries = QueryManager()


class VoteManager:
    def __init__(self):
        self.db = Database

    @log_decorator
    def insert_votes(self):
        """
        Insert a new vote into the votes table
        """
        try:
            tender.view_tenders()
            tender_id = int(input("Enter the tender ID: "))
            user_id = queries.check_user_is_login()

            query = '''
                INSERT INTO votes (tender_id, user_id)
                VALUES (%s, %s);
                '''
            values = (tender_id, user_id)
            execute_query(query, values)
            print("Vote added successfully!")
            return True
        except ValueError:
            print("Invalid input. Please try again.")
            return False
        except Exception as e:
            print(f"Error: {e}")
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
            if result:
                print("Votes:")
                for row in result:
                    print(f"Vote id: {row[0]}, Tender id: {row[1]}, User id: {row[2]}, vote_value: {row[3]}")
                return True
            else:
                print("No votes found.")
                return False
        except Exception as e:
            print(f"An error occurred while viewing votes: {str(e)}")
            return False
