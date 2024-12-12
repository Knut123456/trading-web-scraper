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
    
    column_names = [desc[0] for desc in cursor.description]

    conn.close()
    
    new_myresult = myresult
    new_column_names = column_names
    return new_myresult, new_column_names
database_info()
