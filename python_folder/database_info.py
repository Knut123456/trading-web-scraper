def database_info():
    from connect_to_database import connect_to_database
    from datetime import datetime, timedelta
    from csv_file_to_database import csv_file_to_database
    conn = connect_to_database()

    cursor = conn.cursor()
    
    # Execute the SHOW TABLES query
    table = csv_file_to_database()

    cursor.execute(f"SELECT * FROM {table}")
    myresult = cursor.fetchall()

    conn.close()

    new_myresult = myresult
    return new_myresult
database_info()
