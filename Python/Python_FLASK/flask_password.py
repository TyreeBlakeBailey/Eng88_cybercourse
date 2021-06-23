import password_functions_Flask as password_functions
from flask import Flask, request, abort

def Test_fun():
    return True


app = Flask(__name__)

@app.route('/anylse/<string:user_pw>')
def pass_checker(user_pw):
    return password_functions.strength_checker(user_pw)

@app.route('/passgen')
def pass_generate():
    return password_functions.pass_generate()

@app.route('/welcome/<string:first_name>/<string:last_name>/<int:dob_day>/<int:dob_month>/<int:dob_year>')
def Welcome(first_name, last_name, dob_day, dob_month, dob_year):
    return password_functions.welcome(first_name, last_name, dob_day, dob_month, dob_year)
