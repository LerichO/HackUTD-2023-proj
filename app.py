
# import proper libraries
from flask import Flask, render_template, request
from flask_pymongo import PyMongo # for later
import model
import math
import os

# initialization
app = Flask(__name__)

monthlyCarPayment = 0
studentLoanPayment = 0
estMonthlyMortgagePayment = 0
creditScore = 0
grossMonthlyIncome = 0
monthlyCreditCardPayment = 0
homeAppraisedValue = 0
downPaymentAmount = 0

# -- Routing --

# -- main page --
# do we need the get request?
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method() == "POST":
        # take in data from questionnare thing
        # print message placeholder
        print("Nice")
        return render_template("index.html")
    else:
        return render_template("index.html")

# -- general stats from dataset --
# eventually to rename or specialize this page
@app.route("/stats", methods=["GET", "POST"])
def stats():
    return render_template("<p>Hello stats page</p>")

# -- results from questionnaire
@app.route("/results", methods=["GET", "POST"])
def results():
    return render_template("<p>Hello results page</p>")

if __name__ == "__main__":
    app.run()