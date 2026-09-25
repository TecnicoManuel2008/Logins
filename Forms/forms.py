from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField,  PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# CLASS FORMULATORIO
class FormCadastro(FlaskForm):
    # criar os inputs
    
    nome = StringField("Nome", validators=[DataRequired()])
    email = EmailField("Emall", validators=[
        DataRequired(), 
        Email(message="Tem que digitar @")
    ])
    senha = PasswordField("Senha", validators=[
       DataRequired(message="Vc tem que digitar algo"), 
       Length(min=8, max=15, message="À senha precisa ter 8 letras")
    ])
    confirm = PasswordField("confirmar", validators=[
       EqualTo("senha", message="Essa password tem que igual a primeira")
       
    ])
    enviar = SubmitField("Enviar")
