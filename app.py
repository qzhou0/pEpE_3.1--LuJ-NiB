from flask import Flask, render_template, redirect, url_for

app = Flask(__name__);

@app.route("/")
def root():
    '''If user not logged in, redirect to landing page. Otherwise redirect to welcome page'''
    return redirect(url_for("landing"))

@app.route("/splash")
def landing():
    '''renders splash (landing) page'''
    return render_template("splash.html")

@app.route("/login", methods=["POST"])
def redir():
    '''redirect to welcome page when login successful'''
    return redirect(url_for("welcome"))

@app.route("/welcome")
def welcome():
    '''welcomes user'''
    return render_template("welcome.html", name='bni')

@app.route("/logout", methods=["POST"])
def logout():
    '''ends session, redirect back to landing page'''
    return redirect(url_for("landing"))

@app.route("/browse")
def library():
    '''renders a list of stories'''
    return render_template("library.html", stories=[])

@app.route("/edit")
def edit():
    '''edit page for story'''
    return render_template("storybase.html", title="", content="")

app.debug = True
app.run()
