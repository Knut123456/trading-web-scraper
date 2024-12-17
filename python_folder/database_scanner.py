def database_scanner():
    from pathlib import Path
    import sys
    parent_div = Path(__file__).parent
    sys.path.append(str(parent_div))
    from connect_to_database import connect_to_database_def
    from datetime import datetime, timedelta

    now = datetime.now()
    
    conn = connect_to_database_def("trading_web_scraper")

    cursor = conn.cursor()

    # Execute the SHOW TABLES query
    cursor.execute("SHOW TABLES")

    # Fetch the results
    tables = cursor.fetchall()

    # Print each table name
    #print("Tables in the database:")
    for table in tables:

        
        edited = table[0]  # Each row is a tuple, so access the first element
        #print(table) #
        split_result_1 = edited.split('_')
        #print(split_result_1)
        year = int(split_result_1[3])
        month = int(split_result_1[4])
        day = int(split_result_1[5])
        hour = int(split_result_1[6])
        minute = int(split_result_1[7])
        second = int(split_result_1[8])  

        date_time_obj = datetime(year, month, day, hour, minute, second)
        drop_table = table[0]

        difference = now - date_time_obj
        if difference > timedelta(hours=2):
            cursor.execute(f"DROP TABLE {drop_table};")
            print(f"removed table {drop_table}")
    conn.close()

database_scanner()
