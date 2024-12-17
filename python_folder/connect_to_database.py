
def connect_to_database(database):
    from python_folder.append_path import append_paths
    append_paths() 
    import mysql.connector
    from mysql.connector import Error
    from dotenv import load_dotenv
    import os

    # Load environment variables from .env file

    load_dotenv()
    if database == "trading_web_scraper":
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")
        port = os.getenv("port")

    elif database == "trading_web_scraper_usefull_info":
        host = os.getenv("DB_HOST_USEFULL_INFO")
        user = os.getenv("DB_USER_USEFULL_INFO")
        password = os.getenv("DB_PASSWORD_USEFULL_INFO")
        database = os.getenv("DB_NAME_USEFULL_INFO")
        port = os.getenv("port_USEFULL_INFO")

    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port 
        )
        if conn.is_connected():
           #print(f"Connected to database ,{database}")
            return conn
            
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")

    return None 

connect_to_database("trading_web_scraper")