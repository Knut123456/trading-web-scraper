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

#from python_folder/webscraper.py import web_scraper


app = Flask(__name__)

#web_scraper()
new_myresult, new_column_names = database_info()

#print(new_column_names)
#print(new_myresult)

csv_scanner()
web_scraper()
csv_file_to_database()


@app.route("/")
def index():
    return render_template("index.html",new_column_names, new_myresult)

if __name__=="__main__":
      # Initialize the scheduler
    scheduler = BackgroundScheduler()

    # Schedule `scheduled_tasks` to run every minute
    scheduler.add_job(scheduled_tasks, IntervalTrigger(minutes=1))

    # Start the scheduler
    scheduler.start()

    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler when the app exits
        scheduler.shutdown()