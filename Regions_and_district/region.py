from database_config.db_settings import execute_query


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
