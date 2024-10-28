from main import app, render_template



#? rotas
@app.route("/")
def homepage():
    return render_template("index.html")