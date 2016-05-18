from flask import render_template, request
from app import app
import cracker 

"""
Handle errors if a page is not found
"""
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

"""
Provide the home page
"""
@app.route("/")
@app.route("/index/")
@app.route("/home/")
def index():
	return render_template("index.html", title="Cyber Security Awareness Module")

"""
Provide page for an "about" section
"""
@app.route("/about/")
def about():
	return render_template("about.html", title="About Us")

"""
Provide page for contact info
"""
@app.route("/contact/")
def contact():
	return render_template("contact.html", title="Contact Info")

"""
Provides page for password module
"""
@app.route("/password-module/")
def passwordModule():
	return render_template("password-module.html", title="Passwords")

"""
Pages for the password cracking exercises

If a GET request is sent, serve the page that takes a password from the user

If a POST request is sent, get the password provided and serve a page with the 
results of the password cracking
"""
@app.route("/password-cracking/", methods=["POST", "GET"])
def passwordCracking():
	if request.method == "GET":
		return render_template("password-cracking.html", title="Password Cracking")
	elif request.method == "POST":
		password = request.form["password"]
     	x = [cracker.makeCrackTable(password, "dict"), cracker.makeCrackTable(password, "brute")]
     	return render_template("password_cracking_results.html", results=x, title="Password Cracking Results")
	

"""
Pages for password strength exercises

If a GET request is sent, serve the page that takes a password from the user

If a POST request is sent, get the password provided and serve a page with the 
results of the password strength test
"""
@app.route("/password-strength/", methods=["GET","POST"])
def passwordStrength():
	if request.method == "POST":
		password = request.form["password"]
		return render_template("password_strength_results.html", results=cracker.makeComplexityTable(password), time=cracker.timeToCrack(password), title="Password Strength Results")
	elif request.method == "GET":
		return render_template("password-strength.html", title="Password Strength")
	

"""
Serve template that is for default passwords
"""
@app.route("/default-passwords/")
def defaultPasswords():
    return render_template("defaultPasswords.html", title="Default Passwords")

"""
Serve template that provides a certificate to the user
"""
@app.route("/password-completion/")
def passwordCompletion():
        return render_template("password-completion.html", title="Password Module Complete")

"""
Provide pages for social engineering and phishing
"""
@app.route("/social-engineering/")
def socialEngineeringModule():
	return render_template("socialengineering-module.html", title="Social Engineering")

"""
Serve template for phishing page 
"""
@app.route("/phishing/")
def phishing():
	return render_template("phishing.html", title="Phishing")

"""
Server template providing techniques to mitigate phishing
"""
@app.route("/detecting-phishing/")
def detectingPhishing():
	return render_template("detectingPhishing.html", title="Detecting Phishing")

"""
Serve template that acts as a fake Cougarnet sign in page
"""
@app.route("/fake-login/")
def fakeLogin():
	return render_template("displaylogin.html")

"""
Serves template relating to browser security
"""
@app.route("/web-security/")
def webSecurity():
	return render_template("web_sec.html")

"""
Serve a template that asks the user to select phishing emails if a GET
request is recieved 

If the user selects the correct checkboxes, serve a page that tells them
they checked the correct boxes, otherwise serve one indicating incorrect results
"""
@app.route("/email-phishing/", methods=["GET", "POST"])
def emailPhishing():
	if request.method == "POST":
		if request.form["submit"] == "submit":
			selected = request.form.getlist("check")
			if "1" in selected and "2" in selected:
				return render_template("email_phishing_results.html", results=True)
			else:
				return render_template("email_phishing_results.html", results=False)
	elif request.method == "GET":
		return render_template("email_phishing.html")
