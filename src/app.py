
from pickle import FALSE
from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)

##########CONEXION DB##############
mysql = MySQL(app)

##########RUTA NO ENCONTRADA##############

def nofound(error):
    return jsonify({
        "res": False,
        "msg": "ruta no encontrada"
    })

#######################RUTAS############################

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "res": "true",
        "msg": "Home amiguito.. navega a otra ruta plz"
    })

@app.route('/carta', methods=['GET'])
def getcarta():
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM libros"
        cur.execute(sql)
        datos = cur.fetchall()
        libros = []
        for fila in datos:
            curso = {'id': fila[0], 'titulo': fila[1],
                     'editorial': fila[2], 'isbn': fila[3], 'precio': fila[4]}
            libros.append(curso)
        return jsonify({'res': True, 'libros': libros})
    except Exception as ex:
        return jsonify({'res': FALSE, 'msg': "Upss..."})

@app.route('/carta/<idlibro>', methods=['GET'])
def getcartaid(idlibro):
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM libros where id = '{0}'".format(idlibro)
        cur.execute(sql)
        fila = cur.fetchone()
        print(fila)
        libro = {'id': fila[0], 'titulo': fila[1],
                 'editorial': fila[2], 'isbn': fila[3], 'precio': fila[4]}

        return jsonify({'res': True, 'libros': libro})

    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

@app.route('/carta', methods=['POST'])
def postcarta():
    try:
        cur = mysql.connection.cursor()
        sql = "INSERT INTO libros (titulo, editorial, isbn, precio) VALUES('{0}','{1}','{2}','{3}')".format(
            request.json['titulo'], request.json['editorial'], request.json['isbn'], request.json['precio'])
        cur.execute(sql)
        mysql.connection.commit()
        return jsonify({
            "res": True,
            "msg": "listo bro , ya esta actualizado"
        })
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

##############________________MAIN_________________-##############
if (__name__ == '__main__'):
    app.config.from_object(config['development'])
    app.register_error_handler(404, nofound)
    app.run()
