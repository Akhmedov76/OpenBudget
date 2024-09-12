from database_config.db_settings import execute_query


def check_user_is_login():
    query = "SELECT * FROM users WHERE status=TRUE"
    result = execute_query(query, fetch="one")
    return result['id']


if __name__ == '__main__':
    user_id = check_user_is_login()
    print(f"User ID: {user_id}")
