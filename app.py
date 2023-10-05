import json

from flask import Flask, jsonify, make_response, request
from controllers import model_controller
from waitress import serve

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    return jsonify(message='Hello from root!')


@app.route("/hello")
def hello():
    return jsonify(message='Hello from path!')


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


@app.route('/predict', methods=['POST'])
def getResult():
    req = request.json
    results = model_controller.predict(req["imagen"])
    return jsonify(results)

@app.route('/predict/url', methods=['POST'])
def getResultURL():
    req = request.json
    results = model_controller.predictImgCargada(req["imagen"])
    return jsonify(results)


if __name__ == "__main__":
    app.run()
    serve(app, port=5000)