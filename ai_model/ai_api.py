from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("plant_health_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    X = np.array([[data["temp"], data["humidity"], data["watering"], data["soil_moisture"]]])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]

    return jsonify({
        "health_status": int(prediction),
        "advice": "Keep it up 🌿" if prediction == 1 else "Adjust watering or sunlight 🌧️☀️"
    })

if __name__ == "__main__":
    app.run(port=5000)
