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
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jeanpierrenzo1234@localhost:5432/utec'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate=Migrate(app,db)
#Ejecutar el flask db init ->Crea la carpeta migrations
#Borrar la base de datos dropdb y luego crearla de nuevo
#Ejecutar el flask db migrate
#Se creará un archivo
class Usuario(db.Model):
    __tablename__ = 'usuarios_nuevos'
    id = db.Column(db.Integer,  primary_key=True)
    dzname = db.Column(db.String(), nullable=False)
    dzEmail = db.Column(db.String(), nullable=False)
    dzOther_phone = db.Column(db.Integer, nullable = False)
    dzOther_sex = db.Column(db.String(), nullable = False)
    dzMessage = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return f'<Usuario: {self.id}, {self.dzname}, {self.dzEmail}, {self.dzOther_phone}, {self.dzOther_sex}, {self.dzMessage}>'

#db.create_all()

@app.route('/usuarios_nuevos/create', methods=['POST'])
def create_usuario():
    print("usuario_creado")
    try:
        dzname = request.get_json()['dzname']
        dzEmail = request.get_json()['dzEmail']
        dzOther_phone = request.get_json()['dzOther_phone']
        dzOther_sex = request.get_json()['dzOther_sex']
        dzMessage = request.get_json()['dzMessage']
        print(dzname, dzEmail, dzOther_phone, dzOther_sex, dzMessage)

        usuario = Usuario(dzname = dzname, dzEmail = dzEmail, dzOther_phone = dzOther_phone, dzOther_sex= dzOther_sex, dzMessage = dzMessage)
        db.session.add(usuario)
        db.session.commit()
        return jsonify({
            "dzname": usuario.dzname,
            "dzEmail": usuario.dzEmail,
            "dzOther_phone": usuario.dzOther_phone,
            "dzOther_sex": usuario.dzOther_sex,
            "dzMessage": usuario.dzMessage
            })
    except:
        db.session.rollback()
        return "hubo un problema"
    finally:
        db.session.close()


@app.route('/')
def index():
    usuario = Usuario.query.all()
    return render_template('index.html', data=usuario)


if __name__ == '__main__':
    app.run(debug=True, port=5010)