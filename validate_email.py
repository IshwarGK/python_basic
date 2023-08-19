# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello World"

# if __name__ == "__main__":
#     app.run()


import re

def validate_email(email):
    email_regex = r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$"
    match = re.match(email_regex, email)
    if match:
        print("True")
    else:
        print("False")
        
        
validate_email("ishwargmail.com")