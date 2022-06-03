from flask import Flask
from flask import render_template
import base_de_calculo as beta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("web.html")

@app.route("/orbita_planeta/<planeta>/<salida>/<llegada>")
def orbitas(planeta,salida,llegada):
    x = beta.Planeta(planeta, salida, llegada)
    return{
        "x": x.x,
        "y": x.y,
        "z": x.z,
        "r0": x.r0,
        "rf": x.rf,
    }

@app.route("/maniobra/<planeta1>/<planeta2>/<salida>/<llegada>")
def maniobra(planeta1, planeta2, salida, llegada):
    viaje = beta.Manniobra2()
    viaje.lambert(planeta1, planeta2, salida, llegada)
    return{
        "man": viaje.coordenadas,
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000)