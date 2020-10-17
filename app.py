from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for, 
    jsonify
)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://student@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Usuario(db.Model):
    __tablename__ = 'usuarios_nuevos'
    id = db.Column(db.Integer,  primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable = False)
    telefono = db.Column(db.Integer, nullable = False)
    mensaje = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return f'<Usuario: {self.id}, {self.nombre}, {self.email}, {self.telefono}, {self.mensaje}>'

@app.route('/todos/create', methods=['POST'])
def create_usuario():
    print("usuario_creado")
    try:
        nombre = request.get_json()['nombre']
        email = request.get_json()['email']
        telefono = request.get_json()['telefono']
        mensaje = request.get_json()['mensaje']

        usuario = Usuario(nombre = nombre, email = email, telefono = telefono, mensaje = mensaje)
        db.session.add(usuario)
        db.session.commit()
        return jsonify({
            "nombre": usuario.nombre
            "email" : usuario.email
        })
    except:
        db.session.rollback()
    finally:
        db.session.close()


@app.route('/')
def index():
    usuario = Todo.query.all()
    return render_template('index.html', data=todos)


if __name__ == '__main__':
    app.run(debug=True, port=5010)
