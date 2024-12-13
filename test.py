import sys
from pathlib import Path
try: 
    from .python_folder.connect_to_database import connect_to_database
    from .python_folder.webscraper import web_scraper
    from .python_folder.csv_scanner import csv_scanner
    from .python_folder.csv_file_to_database import csv_file_to_database
    from .python_folder.database_info import database_info 
    from .python_folder.database_scanner import database_scanner 
    from .python_folder.connect_to_database import connect_to_database   

    print("Python is searching for modules in these paths:")
    for path in sys.path:
        print(path)
finally:
    print("Python is searching for modules in these paths:")
    for path in sys.path:
        print(path)

    current_dir = Path(__file__).parent
    python_folder = current_dir / "python_folder"

    # Check the type of python_folder
    print(f"Type of python_folder: {type(python_folder)}")

    # Convert to string before appending
    sys.path.append(str(python_folder))
    print("Updated sys.path:")
    print("\n".join(sys.path))