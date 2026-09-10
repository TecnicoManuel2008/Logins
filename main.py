# mini-projecto: cadastro de clientes

from flask import Flask, session, request, redirect, url_for, render_template
from models.models import Cliente, Session
from Forms.forms import FormCadastro

from hashlib import sha256

app = Flask(__name__)

# depois vou modificar essa chave
app.config["SECRET_KEY"] = "12345678"


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
            user = Cliente(nome=nome, email=email, hash=hashsenha, senha=hashsenha)
            sessao.add(user)
            sessao.commit()
            
        session['user'] = nome
        session["logado"] = True
        
        return "ligado ..."
        
    return redirect(url_for('index'))
        

@app.route("/perfil")
def perfil():
    return f"Perfil senhor(a) {session['user']} "
    
    
if __name__ == '__main__':
    app.run(debug=True)
    