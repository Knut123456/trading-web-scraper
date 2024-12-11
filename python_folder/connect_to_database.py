
def connect_to_database():
    import mysql.connector
    from mysql.connector import Error
    from dotenv import load_dotenv
    import os

    # Load environment variables from .env file

    load_dotenv()
    
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    port = os.getenv("port")

    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port 
        )
        if conn.is_connected():
            print(f"Connected to database ,{database}")
            return conn
            
    except Error as e:
        print(f"Error while connecting to MariaDB: {e}")

    return None 

connect_to_database()