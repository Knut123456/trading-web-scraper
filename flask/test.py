from flask import Flask,render_template 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultat", methods=["POST"])
def resultat():
    return render_template("resultat.html")

@app.route("/meny")
def meny():
    return render_template("meny.html")
if __name__=="__main__":
    app.run(debug=True)