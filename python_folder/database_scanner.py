
def database_scanner ():

    from connect_to_database import connect_to_database
    conn = connect_to_database()

    cursor = conn.cursor()

    show_tables = cursor.execute("SHOW TABLES")

    print(show_tables)
    conn.close()

database_scanner ()