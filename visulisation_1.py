import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("🌿 Starting Data Visualization for Indoor Plant Dataset...\n")

# 1️⃣ Load the cleaned dataset
file_path = "Cleaned_Indoor_Plant_Data.csv"
df = pd.read_csv(file_path)

print("✅ Dataset loaded successfully!")
print(f"📊 Shape: {df.shape}\n")
print(df.head())

# 2️⃣ Basic statistics overview
print("\n📈 Dataset Summary:")
print(df.describe())

# 3️⃣ Plot Health Score distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Health_Score', data=df, palette='Greens')
plt.title('Distribution of Plant Health Scores')
plt.xlabel('Health Score (1 = Poor, 5 = Excellent)')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 4️⃣ Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
plt.title('Correlation Heatmap Between Features')
plt.tight_layout()
plt.show()

# 5️⃣ Relationship between environmental factors and health
plt.figure(figsize=(7,5))
sns.scatterplot(x='Humidity_%', y='Health_Score', data=df, color='green')
plt.title('Humidity vs Health Score')
plt.xlabel('Humidity (%)')
plt.ylabel('Health Score')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
sns.scatterplot(x='Room_Temperature_C', y='Health_Score', data=df, color='orange')
plt.title('Temperature vs Health Score')
plt.xlabel('Room Temperature (°C)')
plt.ylabel('Health Score')
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
sns.scatterplot(x='Soil_Moisture_%', y='Health_Score', data=df, color='blue')
plt.title('Soil Moisture vs Health Score')
plt.xlabel('Soil Moisture (%)')
plt.ylabel('Health Score')
plt.tight_layout()
plt.show()

# 6️⃣ Boxplot for Watering Frequency vs Health Score
plt.figure(figsize=(7,5))
sns.boxplot(x='Health_Score', y='Watering_Frequency_days', data=df, palette='Set2')
plt.title('Watering Frequency vs Plant Health')
plt.xlabel('Health Score')
plt.ylabel('Watering Frequency (days)')
plt.tight_layout()
plt.show()

print("\n✅ Visualization Completed Successfully! 🌸")
