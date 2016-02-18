from flask import render_template
from app import app

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template("index.html", title="Cyber Security Awareness Module")

@app.route("/password-cracking/")
def passwordCracking():
	return render_template("password-cracking.html", title="Password Cracking")

@app.route("/password-strength/")
def passwordStrength():
	return render_template("password-strength.html", title="Password Strength")
