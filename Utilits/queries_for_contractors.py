from Database_config.db_settings import Database, execute_query
from Decorator.decorator import log_decorator


class ContractorManager:
    def __init__(self):
        self.db = Database

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
            if result:
                print("Contractors:")
                for row in result:
                    print(
                        f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]},"
                        f" Contact Person: {row[3]}, Contact Number: {row[4]}, Address: {row[5]}")
                return True
            else:
                print("No contractors found.")
                return False
        except Exception as e:
            print(f"An error occurred while viewing contractors: {str(e)}")
            return False
