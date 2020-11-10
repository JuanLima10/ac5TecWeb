from flask import Flask, render_template, request, url_for, redirect, g ,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost/ac5'
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'tbUsuario'
    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeUsuario = db.Column(db.String(225))
    userUsuario = db.Column(db.String(25))
    senhaUsuario = db.Column(db.String(25))
    def __init__(self, nomeUsuario, userUsuario, senhaUsuario):
        self.nomeUsuario = nomeUsuario
        self.userUsuario = userUsuario
        self.senhaUsuario = senhaUsuario

db.create_all()

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == "POST":
        nomeUsuario = (request.form.get("nome"))
        userUsuario = (request.form.get("username"))
        senhaUsuario = (request.form.get("senha"))
        confSenha = (request.form.get("confSenha"))
        if senhaUsuario != confSenha:
            return redirect(url_for("cadastro"))
        else:
            if nomeUsuario:
                a = Usuario(nomeUsuario, userUsuario, senhaUsuario)
                db.session.add(a)
                db.session.commit()
    return redirect(url_for("cadastro"))

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/competidores")
def competidor():
    return render_template("competidores.html")

if __name__ == "__main__":
    app.run(debug=True)