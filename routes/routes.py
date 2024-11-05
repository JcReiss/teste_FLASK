from main import app, render_template



#? rotas
@app.route("/")
def homepage():
    return render_template("index.html")
    

#? rota "sobre"
@app.route("/sobre")
def rota_sobre():
    return "conheça nosso site"


@app.route("/cadastro")
def rota_cadastro():
    return "faça seu cadastro aqui"