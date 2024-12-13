from flask import Flask, render_template, request, redirect, url_for, flash
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import sys

from python_folder  import web_scraper, csv_scanner , csv_file_to_database, database_info, database_scanner, connect_to_database
""" current_dir = Path(__file__).parent
python_folder = current_dir.parent /"python_folder"
sys.path.append(str(python_folder))
 """

""" from webscraper import web_scraper
from csv_scanner import csv_scanner
from csv_file_to_database import csv_file_to_database
from database_info import database_info 
from database_scanner import database_scanner 
from connect_to_database import connect_to_database  """

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
    #print(new_myresult)
    
        

@app.route("/table")
@app.route("/page/<int:page>")
def table(page = 1):
    rows_per_page = 10
    start = (page - 1) * rows_per_page
    #print(new_myresult)  
    end = start + rows_per_page
    paginated_results = new_myresult[start:end]
    total_pages = -(-len(new_myresult) // rows_per_page)
    return render_template("table.html", 
                        column_names=new_column_names, 
                        results=paginated_results, 
                        current_page=page, 
                        total_pages=total_pages)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():
    return render_template('account.html')
    
@app.route('/create_account', methods=['POST'])
def create_account():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        conn = connect_to_database("trading_web_scraper_usefull_info")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (username, password, email) VALUES  ({username}, {password}, {email}")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.form.get('username')
        password = request.form.get('password')
        conn = connect_to_database("trading_web_scraper_usefull_info")
        cursor = conn.cursor()
        username = cursor.execute("select * from username" )
        password = cursor.execute("select * from password" )
        # Validate the user
        if username in users and users[username] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('login'))
    



if __name__=="__main__":
      # Initialize the scheduler
    scheduler = BackgroundScheduler()

    # Schedule `scheduled_tasks` to run every minute
    scheduler.add_job(colletction, IntervalTrigger(minutes=1))

    # Start the scheduler
    scheduler.start()

    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler when the app exits
        scheduler.shutdown()