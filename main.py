from flask import Flask,url_for, render_template
from flask import blueprints

app =  Flask(__name__)

from routes.routes import *


if __name__ == "__main__":
    app.run(debug=True) 