from flask import Flask, render_template, request

from motordesigner.motor_designer import calculate_torque as calc_torque

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate/torque/', methods=['POST'])
def calculate_torque():
    pn: float = float(request.form['pn'])
    speed: float = float(request.form['speed'])
    torque: float = calc_torque(pn, speed)
    return render_template('torque_result.html', pn=pn, speed=speed, torque=torque)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
