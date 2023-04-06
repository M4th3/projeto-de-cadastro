from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models_forms import db, Usuario, Cidade, Form_cidade_usuario

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meu_projeto.db"
app.config["SECRET_KEY"] = '123d2ab56c6f29576655fae9db16c1e4f6e3c9e4e88e745d4bd588ef2ead9d05'
db.init_app(app)


with app.app_context(): 
    db.create_all()  



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users_list():
    resultado = db.session.execute(db.select(Usuario).order_by(Usuario.nome)).scalars() 
    return render_template('users.html', users=resultado)   
                
@app.route('/users/create', methods=['POST', 'GET'])
def usercreate():
    form = Form_cidade_usuario()
    if form.validate_on_submit():
        user=Usuario(nome=form.nome_do_usuario.data, idade=form.idade.data, cpf=form.cpf.data)
        cidade = Cidade(mun=form.nome_do_mun.data, UF=form.estado.data)
        db.session.add(user)
        db.session.add(cidade)
        db.session.commit()
        redirect(url_for('users_list'))
    return render_template('create.html', form=form )

@app.route('/users/delete', methods=['POST', 'GET'])
def users_delete():
    if request.method=='POST':
        usuario_nome = request.form['usuário']
        user = db.session.execute(db.select(Usuario).filter_by(nome=usuario_nome)).scalar()
        db.session.delete(user)
        db.session.commit()    
        return redirect(url_for('users_list'))
    
    return render_template('delete.html')
 
@app.route('/users/update', methods=['POST', 'GET'])
def users_update():
    if request.method == 'POST':
        form = Form_cidade_usuario()
        nome = form.nome_do_usuario.data
        user = db.session.execute(db.select(Usuario).filter_by(nome= nome))
        user.nome = form.nome_do_usuario.data
        user.idade = form.nome_do_usuario.data
        user.cpf = form.cpf.data 
        print(user.cpf)

        db.session.commit()
        redirect(url_for('users_list'))  

    return render_template('update.html')



if __name__ == '__main__':
     app.run(debug=True, port=8000)