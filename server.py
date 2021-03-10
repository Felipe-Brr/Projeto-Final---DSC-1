from flask import Flask
from Arduino import Arduino
from ArduinoDAO import ArduinoDAO

app = Flask(__name__)


@app.route("/gravar/<v1>/<v2>/<v3>")
def gravar(v1, v2, v3):
    v1 = int(v1)
    v2 = int(v2)
    v3 = int(v3)
    if 0 < v1 <= 200:
        if v2 == 0 or v2 == 1:
            if 0 < v3 <= 400000:  # TSL2561
                v1 = str(v1)
                v2 = str(v2)
                v3 = str(v3)

                arduino = Arduino(v1, v2, v3)
                dao = ArduinoDAO()
                dao.create(arduino)
                return "Temperatura: " + v1 + " Presença: " + v2 + " Luminosidade: " + v3
            else:
                return "Sensor de luminosidade com problemas"
        else:
            return "Sensor de presença com problemas"
    else:
        return "Sensor de temperatura com problemas"

app.run(host="0.0.0.0", port="8000")