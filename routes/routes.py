from main import app, render_template



#? rotas
@app.route("/")
def homepage():
    return render_template("index.html")
    

#? rota "sobre"
@app.route("/sobre")
def rota_sobre():
    return render_template("sobre.html")
