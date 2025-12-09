from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    r = request.form.get("q")
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/dbs", methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/DBSPrediction", methods=["GET","POST"])
def DBSPrediction():
    q = float(request.form.get("q"))
    model = joblib.load("dbs.jl")
    r = model.predict([[q]])
    return(render_template("DBSPrediction.html",r=r[0][0]))

@app.route("/Credit", methods=["GET","POST"])
def Credit():
    return(render_template("Credit.html"))

@app.route("/creditPrediction", methods=["GET","POST"])
def creditPrediction():
    q = float(request.form.get("q"))
    model = joblib.load("/workspaces/W1-6007/german_credit.pkl")
    r = model.predict([[q]])
    if r == 1:
        r = 'Approved'
    else:
        r = 'Not Approved'
    return(render_template("creditPrediction.html",r))

if __name__ == "__main__":
    app.run()