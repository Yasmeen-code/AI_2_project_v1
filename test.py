# 🌸 Flower Classification using KNN
# Dataset: Iris (150 rows, 3 flower species)

# ========== 1. Import Libraries ==========
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ========== 2. Load Dataset ==========
# sklearn فيها dataset جاهز اسمه iris
from sklearn.datasets import load_iris
iris = load_iris()

# نحوله لـ DataFrame علشان نعرضه بسهولة
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print("✅ Dataset Loaded Successfully!")
print(df.head())

# ========== 3. Data Visualization ==========
sns.pairplot(df, hue="species")
plt.suptitle("Flower Features Visualization", y=1.02)
plt.show()

# ========== 4. Data Preprocessing ==========
X = df.drop("species", axis=1)
y = df["species"]

# ========== 5. Split Data ==========
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training samples: {len(X_train)}, Testing samples: {len(X_test)}")

# ========== 6. Train Model ==========
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("✅ Model Trained Successfully!")

# ========== 7. Evaluate Model ==========
y_pred = model.predict(X_test)

print("\n🎯 Model Evaluation:")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ========== 8. Try a Prediction ==========
sample = [[5.1, 3.5, 1.4, 0.2]]  # مثال لقيم زهره
prediction = model.predict(sample)
print("\n🌼 Example Prediction for sample [5.1, 3.5, 1.4, 0.2]:", prediction[0])
