from Database_config.db_settings import execute_query


def region_name():
    query = '''
        INSERT INTO region (region_name) VALUES
            ('Andijon viloyati'),
            ('Buxoro viloyati'),
            ('Jizzax viloyati'),
            ('Qashqadaryo viloyati'),
            ('Navoiy viloyati'),
            ('Namangan viloyati'),
            ('Samarqand viloyati'),
            ('Surxondaryo viloyati'),
            ('Sirdaryo viloyati'),
            ('Toshkent shahri'),
            ('Toshkent viloyati'),
            ('Farg`ona viloyati'),
            ('Xorazm viloyati'),
            ('Qoraqalpog`iston Respublikasi');
            '''
    execute_query(query)
    return True


def get_regions():
    page = int(input("Enter a page(0-10): "))
    query = """
    SELECT * FROM region
    ORDER BY region_id  
    LIMIT 5 OFFSET %s;
    """
    result = execute_query(query, (page,), fetch='all')
    if result:
        for region in result:
            print(f"ID: {region[0]}, Region Name: {region[1]}")
        return True
    else:
        print("No regions found.")
        return None
