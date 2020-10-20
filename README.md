# Proyecto DBP 2020-2 #
#### Integrantes:
1.Marcelo Juan Surco Salas.
2.Harold Alexis Canto Vidal
3.Jean Pier Ángeles.
4.Alberto Domenic Rincon Espinoza.

[ TOC ]

## Descripción del proyecto:
Nuestro proyecto cuenta con un modulo de registro y login a través de back y front end.


## Objetivos principales / Misión / Visión :

### Objetivos:
El objetivo de este proyecto es crear un sistema que nos permitar hacer registros y logeos basandonos en el modelo cliente servidor. 
### Misión:
Relizar todas las implemetaciones de manera correcta y eficaz.
### Visión:
Tener como resultado final un proyecto muy bueno, capaz de funcionar de manera eficiente.

## Back-end /  Front-end / Base de datos:
### Back-end
Utilizamos flask como framework, este nos permite realizar metodos importantes en la app.
### Front-end
En el Front-end hemos utilizado HTML y CSS.
### Base de datos
Hemos utilizado una base de datos relacional, en este caso postgresql, además de utilizar SQLAlchemy como ORM para poder convertir las tablas Clases python y así mismo crear modelos.
## Host
En este caso hemos  utilizado el local host como base de datos, cliente y servidor.
## Forma de autenticación:



## Manejo de errores
El manejo de errores se hace a través de un app.errorhandler como se muestra. Además, se maneja solo los posibles errores que puede haber en la app.
``` python 
@app.errorhandler(404)
def page_not_found(err):
    return render_template("page_not_foud.html"),404

@app.errorhandler(403)
def forbidden(err):
    return render_template("forbidden.html"),403

@app.errorhandler(501)
def not_implemented(err):
    return render_template("not_implemented.html"),501
```
## Request y response
### Response
El response de la data se hace a través de flask, siendo especificos, de la función render_template, donde le enviamos la data al front-end
``` python
@app.route('/')
def index():
    usuario = Usuario.query.all()
    return render_template('index.html', data=usuario)
```
### Request
El request se hace de manera asincrona a través de fetch.
``` js
 document.getElementById('form').onsubmit = function(e) {
                    e.preventDefault();
                    fetch('/usuarios_nuevos/create', {
                        method: 'POST',
                        body: JSON.stringify({
                            'dzname': document.getElementById('dzname').value,
                            'dzEmail': document.getElementById('dzEmail').value,
                            'dzOther_phone': document.getElementById('dzOther_phone').value,
                            'dzOther_sex': document.getElementById('dzOther_sex').value,
                            'dzMessage': document.getElementById('dzMessage').value
                        }),
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(function(response){
                        return response.json();
                    })
                    .then(function(jsonResponse) {
                        document.getElementById('error').className = 'hidden';
                        const liItem = document.createElement('LI');
                        liItem.innerHTML = jsonResponse['dzname'];
                        document.getElementById('usuarios_ingresados').appendChild(liItem);
                        const liItem2 = document.createElement('LI');
                        liItem2.innerHTML = jsonResponse['dzEmail'];
                        document.getElementById('usuarios_ingresados').appendChild(liItem2);
                        const liItem3 = document.createElement('LI');
                        liItem3.innerHTML = jsonResponse['dzOther_phone'];
                        document.getElementById('usuarios_ingresados').appendChild(liItem3);
                        const liItem4 = document.createElement('LI');
                        liItem4.innerHTML = jsonResponse['dzOther_sex'];
                        document.getElementById('usuarios_ingresados').appendChild(liItem4);
                        const liItem5 = document.createElement('LI');
                        liItem5.innerHTML = jsonResponse['dzMessage'];
                        document.getElementById('usuarios_ingresados').appendChild(liItem5);
                        document.getElementById('error').className = 'hidden';
                        })
                    .catch(function(error) {
                        document.getElementById('error').className = '';
                    });
                }
```
## Ejecución del sistema
La ejecución del sistema se hace simplemente corriendo el app.py, ya que tenemos definido una condicional para arrancar el sistema.
``` python
if __name__ == '__main__':
    app.run(debug=True, port=5010)
```

