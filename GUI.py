import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# ========== 1. Load and train the model ==========
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# ========== 2. Create GUI window ==========
root = tk.Tk()
root.title("🌸 Flower Classifier (KNN Model)")
root.geometry("400x400")
root.configure(bg="#F8F8FF")

# ========== 3. Labels and Input Fields ==========
labels = [
    "Sepal length (cm)",
    "Sepal width (cm)",
    "Petal length (cm)",
    "Petal width (cm)"
]

entries = []
for i, label in enumerate(labels):
    tk.Label(root, text=label, bg="#F8F8FF", font=("Arial", 12)).pack(pady=5)
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack()
    entries.append(entry)

# ========== 4. Prediction Function ==========
def predict_flower():
    try:
        values = [float(e.get()) for e in entries]
        sample_df = pd.DataFrame([values], columns=X.columns)
        prediction = model.predict(sample_df)[0]
        messagebox.showinfo("Prediction Result", f"🌼 The flower is likely: {prediction}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# ========== 5. Button ==========
predict_btn = tk.Button(root, text="Predict Flower Type 🌸", command=predict_flower,
                        bg="#9370DB", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
predict_btn.pack(pady=20)

root.mainloop()
