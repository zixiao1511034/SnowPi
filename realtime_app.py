import RPi.GPIO as GPIO
import time
import random
from flask import *


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 19
buttonSts = GPIO.LOW

# Set button and PIR sensor pins as an input
GPIO.setup(button, GPIO.IN)
#GPIO.setup(senPIR, GPIO.IN)


@app.route("/")
def index():
    # Read Sensors Status
    buttonSts = GPIO.input(button)
    templateData = {
        'switch': buttonSts
    }
    return render_template('newindex.html', **templateData)


@app.route('/switch')
def switch():
    def get_switch_value():
        while True:
            buttonSts = GPIO.input(button)
            # use "data": indentical var name with onmessage function in SSE receiver!
            yield "data: {0}\n\n".format(buttonSts)
            time.sleep(1.0)
    return Response(get_switch_value(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
