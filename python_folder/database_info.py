def database_info():
    from pathlib import Path
    import sys
    parent_div = Path(__file__).parent
    sys.path.append(str(parent_div))
    from connect_to_database import connect_to_database_def
    from datetime import datetime, timedelta
    from csv_file_to_database import csv_file_to_database
    conn = connect_to_database_def("trading_web_scraper")

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

