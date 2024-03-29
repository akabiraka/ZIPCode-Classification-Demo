from flask_cors import CORS
from flask import Flask, request, render_template, jsonify
from core.prediction import Prediction
import json

app = Flask(__name__, template_folder='.')
CORS(app)

@app.route("/")
def home():
    "This loads the index.html as home"
    return render_template('index.html')

@app.route("/index", methods=['GET', 'POST', 'OPTIONS'])
def index():
    "This service is just a test, which prints alhumdulillah as json"
    return jsonify("alhumdulillah")

@app.route("/calculate", methods=['POST'])
def calculate():
    """This service takes latitude and longitude call a private function
    to calculate the expected result"""
    lat = float(request.form["lat"])
    lng = float(request.form["lng"])
    prediction = Prediction(lng, lat)
    result = prediction.do_KNN_and_naive_bayes()
    return json.dumps(result)#.to_json()

if __name__ == "__main__":
    app.run()
