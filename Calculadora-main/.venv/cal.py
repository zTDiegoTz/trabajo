from flask import Flask
from flask_cors import CORS
import math as mt
from flask import jsonify


app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")

def suma(numero1 = 0, numero2 = 0):
    resultado = numero1 + numero2
    #return f"el resultado es {resultado}"
    data={
        "resultado": resultado,
        "operacion": "suma"
    }
    return jsonify(data)



@app.route("/")
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")

def resta(numero1= 0, numero2 = 0):
    resultado = numero1 - numero2
    #return (f"la resta es {resultado}")
    data={
        "resultado": resultado,
        "operacion": "resta"
    }
    return jsonify (data)


@app.route("/")
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")

def multipli(numero1, numero2):
    resultado = numero1 * numero2
    #return (f"la resta es {resultado}")
    data={
        "resultado": resultado,
        "operacion": "multiplicacion"
    }
    return jsonify (data)

@app.route("/")
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")
@app.route("/division/<float:numero1>/<float:numero2>")
@app.route("/division/<int:numero1>/<int:numero2>")

def division(numero1, numero2):
    resultado = numero1 / numero2
    #return (f"la resta es {resultado}")
    data={
        "resultado": resultado,
        "operacion": "divicion"
    }
    return jsonify (data)

@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
def potenciacio(numero1 = 0, numero2 = 0):
    resultado = numero1 ** numero2
    #return f"el resultado es: {resultado}"

    data={
        "resultado": resultado,
        "operacion":"potenciacion"
    }
    return jsonify(data)

@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1):
    resultado = mt.sin(numero1)
    #return f"el resultado es {resultado}"
    data = {
        "resultad0": resultado,
        "operacion": "seno"
    }
    return jsonify(data)


@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1):
    resultado = mt.cos(numero1)
    #return f"el resultado es {resultado}"

    data = {
        "resultad0": resultado,
        "operacion": "coseno"
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)