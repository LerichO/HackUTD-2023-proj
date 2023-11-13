
# import proper libraries
from flask import Flask, render_template, request
from flask_pymongo import PyMongo # for later
import pandas
import model
import math
import os
import loan_approval

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
@app.route("/utdhack.html", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("index.html")
    else:
        return render_template("utdhack.html")


# -- general stats from dataset --
# eventually to rename or specialize this page
@app.route("/stats", methods=["GET", "POST"])
def stats():
    return render_template("<p>Hello stats page</p>")

# -- results from questionnaire
@app.route("/info.html", methods=["GET", "POST"])
def results():
    # take in data from questionnare thing
    user_data = {
        'MonthlyMortgagePayment' : [request.form["monthly-mortgage"]],
        'AppraisedValue' : [request.form["home-value"]],
        'CreditCardPayment' : [request.form["credit-card"]],
        'CarPayment' : [request.form["monthly-car"]],
        'StudentLoanPayments' : [request.form["student-loan"]],
        'GrossMonthlyIncome' : [request.form["gross-income"]],
        'DownPayment' : [request.form["down-payment"]],
        'CreditScore' : [request.form["credit-score"]]
    }
    
    user_df = pandas.DataFrame(user_data, index = [0])

    # to replace this df definition with reference to MongoDB database upload
    home_buyer_df=pandas.read_csv("https://raw.githubusercontent.com/LerichO/HackUTD-2023-proj/main/labelled.csv")
    home_buyer_df.drop(columns=['Approved', 'Reasons'])
    print("user input accepted")

    # run input data through loan_approval.py
    score, evaluations = loan_approval.approve_func(user_df, home_buyer_df)
    result = ""
    if score == 0:
        result = "Denied"
    elif score == 1:
        result = "Approved"
    # return render_template("info.html", result, evaluations)
    print("result:")
    print(result)
    print("evaluations")
    print(evaluations)
    return render_template("info.html", result = result, evaluations = evaluations)

@app.route("/info.html", methods=["GET", "POST"])
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run()