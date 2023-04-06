from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, InputRequired

db = SQLAlchemy()

class Form_cidade_usuario(FlaskForm):
    nome_do_mun = StringField('Nome da cidade', validators=[DataRequired(), Length(min=3, max=30), InputRequired()])
    estado = StringField('Estado', validators=[Length(min=2, max=2), DataRequired(), InputRequired()])
    nome_do_usuario = StringField('Usuário', validators=[Length(min=2, max=300), DataRequired(), InputRequired()])
    cpf = IntegerField('CPF', validators=[DataRequired(), InputRequired()])
    idade = IntegerField('Idade', validators=[DataRequired(), InputRequired()] )
    submit = SubmitField(label=('Submit'))

class Usuario(db.Model):
    __tablename__ = 'Usuário'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(300), unique=True, nullable=False, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False)
    idade = db.Column(db.Integer, nullable = False)
    id_mun = db.Column(db.Integer, db.ForeignKey("Cidade.id"), nullable=False)

class Cidade(db.Model):
    __tablename__ = 'Cidade'

    id = db.Column(db.Integer, primary_key=True)
    mun = db.Column(db.String(200), nullable=False)
    UF = db.Column(db.String(2), nullable=False)


    
