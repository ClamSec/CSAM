from flask import render_template
from flask import request
from app import app

import hashlib
import cracker

# Handle errors.
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Provide the home page.
@app.route("/")
@app.route("/index/")
@app.route("/home/")
def index():
	return render_template("index.html", title="Cyber Security Awareness Module")

# Provide page for an About section.
@app.route("/about/")
def about():
	return render_template("about.html", title="About Us")

#Provide page for contact info.
@app.route("/contact/")
def contact():
	return render_template("contact.html", title="Contact Info")

# Provide pages for password related modules.
@app.route("/password-module/")
def passwordModule():
	return render_template("password-module.html", title="Passwords")

@app.route("/password-cracking/")
def passwordCracking():
	return render_template("password-cracking.html", title="Password Cracking")

@app.route("/password-cracking/", methods=["POST"])
def passwordCrackingPost():
	password = request.form["password"]
	hashedPassword = hashlib.md5(password.rstrip().encode('utf-8')).hexdigest()
	crackerResults = cracker.dictionaryAttack(hashedPassword)
	return crackerResults

@app.route("/password-strength/")
def passwordStrength():
	return render_template("password-strength.html", title="Password Strength")
