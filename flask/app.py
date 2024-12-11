from flask import Flask,render_template 
from pathlib import Path
from ..python_folder.webscraper import web_scraper
from ..python_folder.csv_scanner import csv_scanner
from ..python_folder.database_info import database_info




app = Flask(__name__)

web_scraper()
info = database_info()
csv_scanner()


@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)