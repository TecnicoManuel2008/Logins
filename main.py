# mini-projecto: cadastro de clientes

# importando as bibliotecas principais
from flask import Flask, session, flash, request, redirect, url_for, render_template
from models.models import Cliente, Session

from sqlalchemy.exc import IntegrityError
from Forms.forms import FormCadastro
from config.config import DevConfig

# utiliasando hashs para criptografar
from hashlib import sha256

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config.from_object(DevConfig)


@app.route('/', methods=['GET'])
def index():
    form = FormCadastro()
    if "user" in session:
       return redirect(url_for('perfil'))

    return render_template("login.html", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():

    form = FormCadastro()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data

        hashsenha = sha256(senha.encode('utf-8')).hexdigest()

        with Session() as sessao:

            try:
                user = Cliente(nome=nome, email=email, hash=hashsenha)
                sessao.add(user)
                sessao.commit()

                session['user_id'] = user.id
                session['user'] = nome
                session["logado"] = True

                flash("Sucesso no login", "sucesso")

                return redirect(url_for("perfil"))

            except ValueError:
                flash("Email já usado", 'Erro')
                return redirect(url_for('index'))

    return redirect(url_for('index'))


@app.route("/perfil")
def perfil():
    if "logado" not in session:

        flash('Tem que fazer Login primeiro ', "Erro")
        return redirect(url_for('index'))

    return render_template("perfil.html", estado=session)

if __name__ == '__main__':
    app.run(debug=True)

