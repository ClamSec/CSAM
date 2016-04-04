from flask import render_template
from flask import request
from app import app

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
    #option = request.form["option"]
    x = [cracker.makeCrackTable(password, 'dict'), cracker.makeCrackTable(password, 'brute')]
    #if option == "dictionary":
    #    return render_template("password_cracking_results.html", results=cracker.makeCrackTable(password, 'dict'), title="Password Cracking Results")
    #else:
    #    return render_template("password_cracking_results.html", results=cracker.makeCrackTable(password, 'brute'), title="Password Cracking Results")
    return render_template("password_cracking_results.html", results=x, title="Password Cracking Results")
@app.route("/password-strength/")
def passwordStrength():
	return render_template("password-strength.html", title="Password Strength")

@app.route("/password-strength/", methods=["POST"])
def passwordStrengthPost():
    password = request.form["password"]
    return render_template("password_strength_results.html", results=cracker.makeComplexityTable(password), time= cracker.timeToCrack(password), title="Password Strength Results")

@app.route("/default-passwords/")
def defaultPasswords():
    return render_template("defaultPasswords.html", title="Default Passwords")

@app.route("/password-completion/")
def passwordCompletion():
        return render_template("password-completion.html", title="Password Module Complete")

# Provide pages for social engineering and phishing.

@app.route("/social-engineering/")
def socialEngineeringModule():
	return render_template("socialengineering-module.html", title="Social Engineering")

@app.route("/phishing/")
def phishing():
	return render_template("phishing.html", title="Phishing")

@app.route("/detecting-phishing/")
def detectingPhishing():
	return render_template("detectingPhishing.html", title="Detecting Phishing")

# Fake CSU login.
@app.route("/fake-login/")
def fakeLogin():
	return render_template("displaylogin.html")

@app.route("/web-security/")
def webSecurity():
	return render_template("web_sec.html")

@app.route("/email-phishing/", methods=['GET', 'POST'])
def emailPhishing():
	if request.method == "POST":
		if request.form['submit'] == 'submit':
			selected = request.form.getlist('check')
			if '1' in selected and '2' in selected:
				return render_template("email_phishing_results.html", results=True)
			else:
				return render_template("email_phishing_results.html", results=False)
	return render_template("email_phishing.html")
