from flask import Flask, render_template, redirect, url_for

app = Flask(__name__);

@app.route("/")
def root():
	return redirect(url_for("landing"))

@app.route("/splash")
def landing():
	return render_template("splash.html")

@app.route("/login")
def redir():
    return redirect(url_for("welcome"))

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

app.run()
