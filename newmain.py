import random
import time
import json
import threading

import thing

from flask import *
import sqlite3

# Create flask app and global pi 'thing' object.
app = Flask(__name__)
pi_thing = thing.PiThing()
_lock = threading.Lock()

def getHistData (numSamples):
    with _lock:
        print("get history data")
        conn = sqlite3.connect('echo.db')
        curs = conn.cursor()
        curs.execute("SELECT * FROM readings ORDER BY time DESC LIMIT "+str(numSamples))
        data = curs.fetchall()
        dates = []
        distances = []
        for row in reversed(data):
            dates.append(row[0])
            distances.append(row[2])
        
        return [dates, distances]

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    # Read the current switch state to pass to the template.
    switch = pi_thing.read_switch()
    # Render index.html template.
    return render_template('history.html', switch=switch)

# # LED route allows changing the LED state with a POST request.
# @app.route("/led/<int:state>", methods=['POST'])
# def led(state):
#     # Check if the led state is 0 (off) or 1 (on) and set the LED accordingly.
#     if state == 0:
#         pi_thing.set_led(False)
#     elif state == 1:
#         pi_thing.set_led(True)
#     else:
#         return ('Unknown LED state', 400)
#     return ('', 204)

# Server-sent event endpoint that streams the switch state every second.
@app.route("/thing")
def thing():
    def read_things_value():
        while True:
            # switch = pi_thing.read_switch()
            thing_state = {
                'switch': pi_thing.read_switch(),
                'echo': pi_thing.read_echo()
            }
            yield 'data: {0}\n\n'.format(json.dumps(thing_state))
            time.sleep(2.0)
    return Response(read_things_value(), mimetype='text/event-stream')


@app.route('/', methods=['POST'])
def my_form_post():

    global numSamples
    global rangeTime
    rangeTime = int(request.form['rangeTime'])
    print(rangeTime)
    numSamples = rangeTime*60//2
    result = getHistData(numSamples)

    histInfo = {
        'rangeTime': rangeTime,
        'hist_date': result[0],
        'hist_dist': list(map(lambda x: x*170, result[1]))
    }
    print(histInfo['hist_dist'])
    #print(histInfo['hist_date'])
    print(len(histInfo['hist_dist']))

    return render_template('history.html', **histInfo)


# @app.route("/history")
# def history():


# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80, threaded=True)
