from flask import Flask,render_template 
from pathlib import Path
from ..python_folder.webscraper import web_scraper
from ..python_folder.csv_scanner import csv_scanner
from ..python_folder.csv_file_to_database import csv_file_to_database



app = Flask(__name__)

web_scraper()
csv_file_to_database()
csv_scanner()


@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)