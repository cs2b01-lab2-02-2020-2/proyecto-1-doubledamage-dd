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
    dzLogueado = db.Column(db.Boolean, nullable = False, default = False)

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



@app.route('/usuario_ingresado/ingreso', methods = ['POST'])
def logeo_usuario():
    try:
        usuario = request.get_json()['usuario']
        telefono = request.get_json()['telefono']
        nombre = Usuario.query.filter_by(dzname = usuario).first()
        clave = Usuario.query.filter_by(dzOther_phone = telefono).first()
        logueado = request.get_json()['logueado']
        if not nombre or not clave:
            print("Porfavor revise si ingresó correctamente el usuario o la contraseña")
            return redirect(url_for('index'))
        else:
            nombre.dzLogueado = logueado
            db.session.commit()
            print('Logueado correctamente')
            return redirect(url_for('next_page'))
    except Exception as e:
        db.session.rollback()
    finally:
        db.session.close()
    return "Logueado correctamente"

@app.route('/')
def index():
    usuario = Usuario.query.all()
    return render_template('index.html', data=usuario)


@app.errorhandler(404)
def page_not_found(err):
    return render_template("page_not_foud.html"),404

@app.errorhandler(403)
def forbidden(err):
    return render_template("forbidden.html"),403

@app.errorhandler(501)
def not_implemented(err):
    return render_template("not_implemented.html"),501


if __name__ == '__main__':
    app.run(debug=True, port=5010)