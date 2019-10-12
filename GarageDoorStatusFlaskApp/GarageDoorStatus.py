from flask import Flask, render_template
from flask_restful import Resource, Api
import time
import datetime
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_12", GPIO.IN)

app = Flask(__name__)
api = Api(app)

class SwitchState(Resource):
	def get(self):
		if GPIO.input("P8_12"):
			sstate = "closed"
		else:
			sstate = "open"

		return {'switch' : sstate}

@app.route("/")
def hello():
	if GPIO.input("P8_12"):
		doorStatus = "closed"
	else:
		doorStatus = "open"

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	templateData = {'title': 'GarageDoorStatus', 'time': st, 'doorStatus':doorStatus}
	return render_template('main.html', **templateData)

api.add_resource(SwitchState,'/api_states')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8124)
