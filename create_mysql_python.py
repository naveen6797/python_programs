def create_database(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        print("database create successfully")
    except Error as err:
        print(f"Error: '{err}'")
create_database_query = "create database mysql_python"
create_database(connect, create_database_query)



 
