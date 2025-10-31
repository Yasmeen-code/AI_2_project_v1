import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("🌱 Starting model training...")

# 1️⃣ Load cleaned dataset
df = pd.read_csv("Cleaned_Indoor_Plant_Data.csv")
print("✅ Data loaded successfully! Shape:", df.shape)

# 2️⃣ Simplify Health Score into Healthy / Unhealthy
df["Health_Status"] = df["Health_Score"].apply(lambda x: 1 if x >= 3 else 0)

# 3️⃣ Drop unnecessary columns
if "Plant_ID" in df.columns:
    df = df.drop(columns=["Plant_ID", "Health_Notes"], errors="ignore")

# 4️⃣ Encode categorical columns
cat_cols = df.select_dtypes(include=["object"]).columns
encoder = LabelEncoder()
for col in cat_cols:
    df[col] = encoder.fit_transform(df[col])

# 5️⃣ Split data
X = df.drop(columns=["Health_Score", "Health_Status"])
y = df["Health_Status"]
feature_names = X.columns  # حفظ الأعمدة الأصلية

# 6️⃣ Standardize numerical data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 7️⃣ Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 8️⃣ Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 9️⃣ Evaluate
y_pred = model.predict(X_test)
print("\n🎯 Model Accuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# 🔟 Save the model, scaler, and feature names
joblib.dump(model, "plant_health_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(list(feature_names), "feature_names.pkl")

print("\n💾 Model, scaler, and feature names saved successfully!")
print("🏁 Training completed.")
