import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("🌿 Smart Plant Care Advisor Starting...\n")

# 1️⃣ Load dataset
print("📥 Loading dataset...")
df = pd.read_csv("Updated_Indoor_Plant_Data_v2.csv")
print("✅ Dataset loaded successfully!\n")
print(df.head())

# 2️⃣ Simplify Health Score into two categories (Healthy / Unhealthy)
df["Health_Status"] = df["Health_Score"].apply(lambda x: 1 if x >= 3 else 0)

# 3️⃣ Drop unneeded columns
for col in ["Plant_ID", "Health_Notes"]:
    if col in df.columns:
        df = df.drop(columns=col)

# 4️⃣ Encode categorical columns (including Plant_Type)
cat_cols = df.select_dtypes(include=["object"]).columns
encoders = {}
for col in cat_cols:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

# حفظ أسماء الأنواع الأصلية
if "Plant_Type" in encoders:
    plant_type_labels = dict(enumerate(encoders["Plant_Type"].classes_))
else:
    plant_type_labels = {}

# 5️⃣ Split features and labels
X = df.drop(columns=["Health_Score", "Health_Status"])
y = df["Health_Status"]

feature_names = X.columns

# 6️⃣ Normalize numeric values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 7️⃣ Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(f"\n📊 Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

# 8️⃣ Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
print("✅ Model trained successfully!\n")

# 9️⃣ Evaluate
y_pred = model.predict(X_test)
print("🎯 Model Evaluation:")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 🔟 User input
print("\n🌱 Enter your plant care details to check health prediction:")

print("\n📘 Example values to help you:")
print("• Soil_Type: 0 = Clay, 1 = Loamy, 2 = Sandy")
print("• Fertilizer_Type: 0 = Organic, 1 = Chemical")
print("• Sunlight_Exposure: 0 = Low, 1 = Medium, 2 = High")
print("• Pest_Presence: 0 = No pests, 1 = Pests detected")
print("• Watering_Amount_ml: between 50–500 depending on plant size")
print("• Room Temperature: usually between 15–30 °C")
print("• Humidity: between 30–80%")
print("• Soil Moisture: between 20–70%")

# 💡 Show available plant types
if plant_type_labels:
    print("\n🌿 Available Plant Types:")
    for k, v in plant_type_labels.items():
        print(f"{k} = {v}")
else:
    print("\n⚠️ No Plant_Type column found in dataset.")

print("----------------------------------------------------")

try:
    temp = float(input("Room Temperature (°C): "))
    humidity = float(input("Humidity (%): "))
    watering_amount = float(input("Watering Amount (ml): "))
    soil_moisture = float(input("Soil Moisture (%): "))
    soil_type = int(input("Soil Type (0=Clay, 1=Loamy, 2=Sandy): "))
    fertilizer_type = int(input("Fertilizer Type (0=Organic, 1=Chemical): "))
    sunlight = int(input("Sunlight Exposure (0=Low, 1=Medium, 2=High): "))

    if plant_type_labels:
        plant_choice = int(input("Choose Plant Type number from the list above: "))
    else:
        plant_choice = 0

    sample_dict = {
        "Height_cm": 25,
        "Leaf_Count": 10,
        "New_Growth_Count": 2,
        "Watering_Amount_ml": watering_amount,
        "Watering_Frequency_days": 3,
        "Room_Temperature_C": temp,
        "Humidity_%": humidity,
        "Fertilizer_Amount_ml": 50,
        "Pest_Severity": 0,
        "Soil_Moisture_%": soil_moisture,
        "Sunlight_Exposure": sunlight,
        "Soil_Type": soil_type,
        "Fertilizer_Type": fertilizer_type,
        "Pest_Presence": 0,
        "Plant_Type": plant_choice,
    }

    # التأكد من أن الأعمدة تتطابق
    for col in feature_names:
        if col not in sample_dict:
            sample_dict[col] = 0

    sample = pd.DataFrame([sample_dict], columns=feature_names)
    sample_scaled = scaler.transform(sample)
    prediction = model.predict(sample_scaled)[0]

    if prediction == 1:
        print("\n✅ Your plant care looks healthy! Keep it up 🌿")
    else:
        print("\n❌ Your plant care might be unhealthy. Try adjusting watering or sunlight 🌧️☀️")

    # 🌿💡 Smart advice
    print("\n💡 Smart Care Advice:")

    if soil_moisture < 30:
        print("💧 The soil is too dry — increase watering slightly.")
    elif soil_moisture > 70:
        print("🚫 Soil too wet — reduce watering to prevent root rot.")
    
    if temp < 18:
        print("❄️ The temperature is low — move the plant to a warmer spot.")
    elif temp > 32:
        print("🔥 Too hot! Consider moving the plant to a cooler area.")

    if humidity < 40:
        print("💨 Air too dry — increase humidity or mist the leaves.")
    elif humidity > 80:
        print("🌫️ High humidity — ensure good ventilation.")

    if sunlight == 0:
        print("🌑 Try placing the plant in a brighter area.")
    elif sunlight == 2:
        print("☀️ Too much direct light — provide some shade.")

    if plant_type_labels:
        print(f"\n🌸 Plant Type Selected: {plant_type_labels.get(plant_choice, 'Unknown')}")

    print("\n🌱 Advice generated successfully!")

except Exception as e:
    print("⚠️ Input skipped or error:", e)

print("\n🏁 Project completed successfully!")
