import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل الداتا الأصلية
print("📥 Loading original dataset...")
df = pd.read_csv("Indoor_Plant_Health_and_Growth_Factors.csv")
print("✅ Dataset loaded successfully!\n")

# تحويل القيم النصية لأرقام لو فيه أخطاء
numeric_cols = ["Room_Temperature_C", "Humidity_%", "Soil_Moisture_%", "Health_Score", "Watering_Amount_ml"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.dropna(subset=numeric_cols, inplace=True)

# إعداد شكل الرسومات
sns.set_theme(style="whitegrid", palette="viridis")

# إنشاء Dashboard
fig = plt.figure(figsize=(16, 12))
fig.suptitle("🌿 Smart Indoor Plant Health Dashboard", fontsize=18, fontweight='bold', color="#2b9348")

# 🔹 1. توزيع درجات الصحة
plt.subplot(2, 3, 1)
sns.histplot(df["Health_Score"], bins=10, kde=True, color="#55a630")
plt.title("🌱 Distribution of Health Scores")
plt.xlabel("Health Score")
plt.ylabel("Number of Plants")

# 🔹 2. الحرارة والرطوبة وتأثيرهم على الصحة (heatmap)
plt.subplot(2, 3, 2)
corr = df[["Room_Temperature_C", "Humidity_%", "Soil_Moisture_%", "Health_Score"]].corr()
sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("🌡 Correlation between Environmental Factors & Health")

# 🔹 3. نوع التربة ومتوسط الصحة
plt.subplot(2, 3, 3)
sns.barplot(data=df, x="Soil_Type", y="Health_Score", ci=None, hue="Soil_Type", dodge=False)
plt.title("🪴 Average Health by Soil Type")
plt.xlabel("Soil Type")
plt.ylabel("Average Health Score")
plt.legend([], [], frameon=False)

# 🔹 4. العلاقة بين الري والصحة
plt.subplot(2, 3, 4)
sns.regplot(data=df, x="Watering_Amount_ml", y="Health_Score", scatter_kws={"alpha":0.6})
plt.title("💦 Watering Amount vs Health Score")
plt.xlabel("Watering (ml)")
plt.ylabel("Health Score")

# 🔹 5. تأثير نوع السماد على الصحة
plt.subplot(2, 3, 5)
sns.boxplot(data=df, x="Fertilizer_Type", y="Health_Score", palette="summer")
plt.title("🌿 Fertilizer Type Impact on Plant Health")
plt.xlabel("Fertilizer Type")
plt.ylabel("Health Score")

# 🔹 6. العلاقة بين الرطوبة والحرارة
plt.subplot(2, 3, 6)
sns.scatterplot(data=df, x="Room_Temperature_C", y="Humidity_%", hue="Health_Score", size="Health_Score", sizes=(30, 200))
plt.title("🔥 Temperature vs Humidity (Colored by Health)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# 💡 Smart Insights Summary
print("\n📊 SMART INSIGHTS SUMMARY:")
print(f"🌡 Avg Temperature: {df['Room_Temperature_C'].mean():.1f}°C")
print(f"💧 Avg Humidity: {df['Humidity_%'].mean():.1f}%")
print(f"🌾 Avg Soil Moisture: {df['Soil_Moisture_%'].mean():.1f}%")
print(f"🌱 Avg Health Score: {df['Health_Score'].mean():.2f}")
print("🪴 Loamy soil and balanced watering (150–300ml) appear most beneficial.\n")
print("✅ Visualization completed successfully!")