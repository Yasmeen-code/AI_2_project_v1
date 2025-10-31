import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

print("📥 Loading dataset...")
df = pd.read_csv("plant_growth_data.csv")  # غيّري اسم الملف لو مختلف
print("✅ Dataset loaded successfully!\n")

print(df.head())
print(f"\nTraining samples: {int(len(df)*0.8)}, Testing samples: {int(len(df)*0.2)}\n")

# ----------------------------
# 🧠 معالجة البيانات (Encoding)
# ----------------------------
label_encoders = {}
for col in df.columns:
    if df[col].dtype == 'object':  # لو العمود فيه نصوص
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# ----------------------------
# ✂️ تقسيم البيانات
# ----------------------------
X = df.drop("Growth_Milestone", axis=1)
y = df["Growth_Milestone"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----------------------------
# 🌳 تدريب النموذج
# ----------------------------
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# ----------------------------
# 🔮 التوقع والتقييم
# ----------------------------
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📊 Mean Squared Error: {mse:.2f}")
print(f"📈 R² Score: {r2:.2f}")

# ----------------------------
# 📉 اختبار على بيانات جديدة
# ----------------------------
sample = pd.DataFrame({
    "Soil_Type": ["loam"],
    "Sunlight_Hours": [7.5],
    "Water_Frequency": ["weekly"],
    "Fertilizer_Type": ["organic"],
    "Temperature": [25],
    "Humidity": [60]
})

# تحويل القيم النصية في المثال إلى أرقام بنفس الـ encoders
for col in sample.columns:
    if col in label_encoders:
        sample[col] = label_encoders[col].transform(sample[col])

prediction = model.predict(sample)
print(f"\n🌱 Predicted Growth Milestone: {prediction[0]:.2f}")
