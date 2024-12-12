from flask import Flask, render_template 
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import sys
current_dir = Path(__file__).parent
python_folder = current_dir.parent /"python_folder"
sys.path.append(str(python_folder))


from webscraper import web_scraper
from csv_scanner import csv_scanner
from csv_file_to_database import csv_file_to_database
from database_info import database_info 
from database_scanner import database_scanner 

#from python_folder/webscraper.py import web_scraper


app = Flask(__name__)
new_myresult = []
new_column_names = []

def colletction():
    global new_myresult, new_column_names
    web_scraper()
    csv_scanner()
    csv_file_to_database()
    database_scanner()
    new_myresult, new_column_names = database_info()


@app.route("/")
@app.route("/page/<int:page>")
def index(page = 1):
    global new_myresult, new_column_names
    rows_per_page = 5
    start = (page - 1) * rows_per_page  
    end = start + rows_per_page
    paginated_results = new_myresult[start:end]
    total_pages = -(-len(new_myresult) // rows_per_page)
    return render_template("index.html", 
                        column_names=new_column_names, 
                        results=paginated_results, 
                        current_page=page, 
                        total_pages=total_pages)

if __name__=="__main__":
      # Initialize the scheduler
    scheduler = BackgroundScheduler()

    # Schedule `scheduled_tasks` to run every minute
    scheduler.add_job(colletction, IntervalTrigger(minutes=1))

    colletction()
    # Start the scheduler
    scheduler.start()

    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler when the app exits
        scheduler.shutdown()