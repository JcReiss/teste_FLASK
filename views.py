from main import app



#? rotas
@app.route("/")
def homepage():
    return "meu site no Flask"