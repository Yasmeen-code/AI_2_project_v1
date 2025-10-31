from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# ✅ تحميل الموديل والـ scaler والـ feature names
model = joblib.load("plant_health_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")  # نفس اللي حفظناه وقت التدريب

@app.route('/')
def home():
    return "✅ AI Model is Running!"
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        temp = float(data["temp"])
        humidity = float(data["humidity"])
        watering = float(data["watering"])
        soil_moisture = float(data["soil_moisture"])

        input_data = pd.DataFrame([{
            "Height_cm": 25,
            "Leaf_Count": 10,
            "New_Growth_Count": 2,
            "Watering_Amount_ml": watering,
            "Watering_Frequency_days": 3,
            "Room_Temperature_C": temp,
            "Humidity_%": humidity,
            "Fertilizer_Amount_ml": 50,
            "Pest_Severity": 0,
            "Soil_Moisture_%": soil_moisture,
            "Sunlight_Exposure": 1,
            "Soil_Type": 1,
            "Fertilizer_Type": 0,
            "Pest_Presence": 0,
        }])[feature_names]

        df_scaled = scaler.transform(input_data)
        prediction = model.predict(df_scaled)[0]

        # ✅ نحول القيمة من numpy int64 إلى int عادي
        prediction = int(prediction)

        if prediction == 1:
            health_status = "✅ Your plant is Healthy!"
            advice = "Keep doing what you're doing 🌿. Everything looks balanced!"
        else:
            health_status = "❌ Your plant might be Unhealthy!"
            advice = "Try adjusting watering or sunlight — your plant may be stressed 🌧️☀️"

        return jsonify({
            "health_status": prediction,
            "message": health_status,
            "advice": advice
        })

    except Exception as e:
        print("⚠️ Error in prediction:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
