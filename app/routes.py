from app import app
from flask import jsonify


info = {
    'current_temp': '-1',
    'desired_temp': '69'
}


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
def get_current_temp():
    return "Current Temperature: " + info["current_temp"]


@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['GET'])
def get_desired_temp():
    return "Desired Temperature: " + info["desired_temp"]


@app.route('/ThermsAreUs/api/v1.0/current-setpoint/<string:new_temp>', methods=['GET', 'PUT'])
def update_desired_temp(new_temp):
    info["desired_temp"] = new_temp
    return get_desired_temp()
