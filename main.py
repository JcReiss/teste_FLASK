from flask import Flask,url_for, render_template


app =  Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug=True) 