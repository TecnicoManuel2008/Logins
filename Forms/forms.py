from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField,  PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# CLASS FORMULATORIO
class FormCadastro(FlaskForm):
    # criar os inputs
    
    nome = StringField("Nome", validators=[DataRequired()])
    email = EmailField("Emall", validators=[
        DataRequired(), 
        Email()
    ])
    senha = PasswordField("Senha", validators=[
       DataRequired(), 
       Length(min=6, max=15, message="À senha precisa ter 8 letras")
    ])
    confirm = PasswordField("confirmar", validators=[
       EqualTo("senha", message="Essa password tem que igual a primeira")
       
    ])
    enviar = SubmitField("Enviar")
