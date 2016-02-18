from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template("index.html", title="Cyber Security Awareness Module")
