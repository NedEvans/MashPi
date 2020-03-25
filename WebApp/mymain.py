import json
import random
import mashthing
import time
from flask import *

# Create flask app and global pi 'thing' object.
app = Flask(__name__)
mash_thing = mashthing.MashThing()

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    # Read the current switch state to pass to the template.
    switch = mash_thing.read_switch()
    pump=mash_thing.read_pump()
    # Render index.html template.
    return render_template('index.html', switch=switch, pump=pump)
    

# LED route allows changing the LED state with a POST request.
# user control of uotput state
@app.route("/led/<int:state>", methods=['POST'])
def led(state):
    # Check if the led state is 0 (off) or 1 (on) and set the LED accordingly.
    if state == 0:
        mash_thing.set_led(False)
    elif state == 1:
        mash_thing.set_led(True)
    else:
        return ('Unknown LED state', 400)
    return ('', 204)

# Server-sent event endpoint that streams the thing state every second.
# streaming input states - display input state!
@app.route('/thing')
def thing():
    def get_thing_values():
        while True:
            # Build up a dict of the current thing state.
            thing_state = {
                'switch': mash_thing.read_switch(),
                'pump': mash_thing.read_pump(),
                'temperature': mash_thing.read_temperature_0(),
                #'humidity': pi_thing.get_humidity()
            }
            # Send the thing state as a JSON object.
            yield('data: {0}\n\n'.format(json.dumps(thing_state)))
            # Wait a second and repeat.
            time.sleep(1.0)
    return Response(get_thing_values(), mimetype='text/event-stream')


# Start the flask debug server listening on the pi port 5000 by default.
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
